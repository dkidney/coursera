import pandas as pd


def kaplan_meier(time, event, expand=False):
	df = pd.DataFrame({
		'time': time,
		'event': event
	}).sort_values(['time', 'event'])

	# times = unique event times
	# d = number of deaths at time t
	# n = number of survivors up to time t
	# times = sorted(list(df['time'][df['event'] == 1].unique()))
	times = sorted(list(df['time'].unique()))
	if times[0] != 0:
		times = [0] + times
	d = []
	n = []

	for t in times:
		d.append(sum((df['time'] == t) & (df['event'] == 1)))
		n.append(sum((df['time'] >= t)))

	d = pd.Series(d)
	n = pd.Series(n)
	p = 1 - (d / n)

	km = pd.DataFrame({
		't': times,
		's': p.cumprod()
	})

	if expand:
		expanded_times = pd.DataFrame(list(range(df['time'].max() + 1)), columns=['t'])
		km = pd.merge(expanded_times, km, how='left', on='t')
		km['s'] = km['s'].ffill().fillna(0)

	return km


# time  = [2, 3, 2, 9, 16, 18, 7, 16, 5, 5]
# event = [1, 0, 1, 1, 1 , 0 , 1, 1 , 1, 0]
# print(kaplan_meier(time, event))
#
# time  = [3, 5, 4, 2]
# event = [1, 1, 0, 1]
# print(kaplan_meier(time, event))

time  = [5, 10, 15]
event = [0, 1, 0]
km = kaplan_meier(time, event)
print(km)
km_e = kaplan_meier(time, event, expand=True)
print(km_e)

if False:
	import matplotlib
	matplotlib.rcParams["backend"]
	km.plot(drawstyle="steps", linewidth=2)
	km.plot(drawstyle="steps-post", linewidth=2)
	km_e.plot(drawstyle="steps", linewidth=2)

	import matplotlib
	matplotlib.use('TkAgg')
	import matplotlib.pyplot as plt
	plt.step(km['t'], km['s'], where='post')
	plt.step(range(len(df.index)),df[1],where='post')
	plt.step(range(len(df.index)),df[2],where='post')