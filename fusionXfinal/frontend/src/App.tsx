import { useMemo, useState } from 'react'
import { BarChart, Bar, LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer, PieChart, Pie, Cell } from 'recharts'

const forecastData = [
  { day: 'Mon', actual: 44, predicted: 42 },
  { day: 'Tue', actual: 49, predicted: 46 },
  { day: 'Wed', actual: 52, predicted: 48 },
  { day: 'Thu', actual: 47, predicted: 46 },
  { day: 'Fri', actual: 60, predicted: 53 },
  { day: 'Sat', actual: 41, predicted: 40 },
  { day: 'Sun', actual: 38, predicted: 37 },
]

const weeklyData = [
  { day: 'Mon', current: 35, previous: 39 },
  { day: 'Tue', current: 41, previous: 44 },
  { day: 'Wed', current: 38, previous: 42 },
  { day: 'Thu', current: 47, previous: 45 },
  { day: 'Fri', current: 52, previous: 50 },
  { day: 'Sat', current: 48, previous: 46 },
  { day: 'Sun', current: 44, previous: 41 },
]

const benchmarkData = [
  { name: 'Building A', value: 12.5, fill: '#34d399' },
  { name: 'Building B', value: 10.1, fill: '#60a5fa' },
  { name: 'Building C', value: 9.8, fill: '#f59e0b' },
]

const recommendations = [
  { action: 'Raise AC setpoint by 2°C', zone: 'Room 203', savings: '8.5 kWh', cost: '$12.75', priority: 'High' },
  { action: 'Turn off lights during daylight', zone: 'Lobby', savings: '3.0 kWh', cost: '$4.50', priority: 'Medium' },
  { action: 'Schedule laundry after 10 PM', zone: 'Service', savings: '5.2 kWh', cost: '$7.80', priority: 'High' },
  { action: 'Clean AC filters', zone: 'All rooms', savings: '2.4 kWh', cost: '$3.60', priority: 'Medium' },
]

const maintenance = [
  { appliance: 'AC - Room 203', status: 'Due soon', next: '2026-09-20' },
  { appliance: 'Fan - Lobby', status: 'Due', next: '2026-09-18' },
  { appliance: 'AC - Hostel A', status: 'Overdue', next: '2026-09-02' },
]

const anomalies = [
  { zone: 'Room 203', risk: 'High', explanation: 'Energy consumption is 44% above expected due to AC operation during low occupancy.' },
  { zone: 'Kitchen', risk: 'Medium', explanation: 'Water heater demand exceeded baseline by 18% during non-peak hours.' },
]

function App() {
  const [setpoint, setSetpoint] = useState(2)
  const [hours, setHours] = useState('18:00-22:00')

  const simulated = useMemo(() => {
    const current = 52.4
    const reduction = Math.min(0.32, 0.05 * setpoint)
    const simulatedDemand = current * (1 - reduction)
    const energySaved = current - simulatedDemand
    const costSaved = energySaved * 1.5
    return { current, simulatedDemand, energySaved, costSaved }
  }, [setpoint])

  return (
    <div className="min-h-screen bg-slate-950 text-slate-100">
      <div className="mx-auto max-w-7xl px-4 py-8">
        <header className="mb-8 flex items-center justify-between">
          <div>
            <p className="text-xs uppercase tracking-[0.2em] text-emerald-400">Smart Energy</p>
            <h1 className="mt-2 text-3xl font-bold">Energy Optimization Dashboard</h1>
          </div>
          <button className="rounded-xl bg-emerald-500 px-4 py-2 font-semibold text-slate-900 hover:bg-emerald-400">Generate Report</button>
        </header>

        <section className="mb-8 grid gap-4 md:grid-cols-5">
          {[
            ['Total Consumption', '198.2 kWh', '+4.8%'],
            ['Estimated Cost', '$278.4', 'This month'],
            ['CO₂ Footprint', '86 kg', 'Lower than last week'],
            ['Active Anomalies', '2', '2 require review'],
            ['Potential Savings', '24.5 kWh', 'Based on top actions'],
          ].map(([label, value, note]) => (
            <div key={label} className="card p-4">
              <p className="text-sm text-slate-400">{label}</p>
              <p className="mt-3 text-2xl font-semibold">{value}</p>
              <p className="mt-2 text-xs text-emerald-300">{note}</p>
            </div>
          ))}
        </section>

        <section className="mb-8 grid gap-6 lg:grid-cols-2">
          <div className="card p-5">
            <h2 className="mb-4 text-lg font-semibold">Energy Forecast</h2>
            <div className="h-72">
              <ResponsiveContainer width="100%" height="100%">
                <LineChart data={forecastData}>
                  <CartesianGrid strokeDasharray="3 3" stroke="#334155" />
                  <XAxis dataKey="day" stroke="#94a3b8" />
                  <YAxis stroke="#94a3b8" />
                  <Tooltip />
                  <Line type="monotone" dataKey="actual" stroke="#f59e0b" strokeWidth={2} />
                  <Line type="monotone" dataKey="predicted" stroke="#34d399" strokeWidth={2} />
                </LineChart>
              </ResponsiveContainer>
            </div>
          </div>

          <div className="card p-5">
            <h2 className="mb-4 text-lg font-semibold">Recommendations</h2>
            <div className="space-y-3">
              {recommendations.map((item) => (
                <div key={item.action} className="rounded-xl border border-slate-700 bg-slate-800/70 p-3">
                  <div className="flex items-center justify-between gap-3">
                    <p className="font-medium text-slate-100">{item.action}</p>
                    <span className="rounded-full bg-emerald-500/20 px-2 py-1 text-xs text-emerald-300">{item.priority}</span>
                  </div>
                  <p className="mt-2 text-sm text-slate-300">Zone: {item.zone}</p>
                  <p className="text-sm text-slate-300">Savings: {item.savings} · Cost: {item.cost}</p>
                </div>
              ))}
            </div>
          </div>
        </section>

        <section className="mb-8 grid gap-6 lg:grid-cols-3">
          <div className="card p-5 lg:col-span-2">
            <h2 className="mb-4 text-lg font-semibold">Weekly Comparison</h2>
            <div className="h-72">
              <ResponsiveContainer width="100%" height="100%">
                <BarChart data={weeklyData}>
                  <CartesianGrid strokeDasharray="3 3" stroke="#334155" />
                  <XAxis dataKey="day" stroke="#94a3b8" />
                  <YAxis stroke="#94a3b8" />
                  <Tooltip />
                  <Bar dataKey="current" fill="#60a5fa" radius={[4, 4, 0, 0]} />
                  <Bar dataKey="previous" fill="#94a3b8" radius={[4, 4, 0, 0]} />
                </BarChart>
              </ResponsiveContainer>
            </div>
          </div>

          <div className="card p-5">
            <h2 className="mb-4 text-lg font-semibold">Peer Benchmark</h2>
            <div className="h-72">
              <ResponsiveContainer width="100%" height="100%">
                <BarChart layout="vertical" data={benchmarkData} margin={{ left: 20 }}>
                  <XAxis type="number" stroke="#94a3b8" />
                  <YAxis type="category" dataKey="name" width={90} stroke="#94a3b8" />
                  <Tooltip />
                  <Bar dataKey="value" radius={[0, 8, 8, 0]}>
                    {benchmarkData.map((entry) => <Cell key={entry.name} fill={entry.fill} />)}
                  </Bar>
                </BarChart>
              </ResponsiveContainer>
            </div>
          </div>
        </section>

        <section className="mb-8 grid gap-6 lg:grid-cols-3">
          <div className="card p-5">
            <h2 className="mb-4 text-lg font-semibold">Maintenance</h2>
            <div className="space-y-3">
              {maintenance.map((item) => (
                <div key={item.appliance} className="rounded-xl border border-slate-700 bg-slate-800/60 p-3">
                  <p className="font-medium">{item.appliance}</p>
                  <p className="mt-1 text-sm text-slate-300">Status: {item.status}</p>
                  <p className="text-sm text-slate-300">Next cleaning: {item.next}</p>
                </div>
              ))}
            </div>
          </div>

          <div className="card p-5">
            <h2 className="mb-4 text-lg font-semibold">Lighting</h2>
            <div className="rounded-xl border border-slate-700 bg-slate-800/70 p-4">
              <p className="text-sm text-slate-300">Daylight available in Lobby and corridor. Turn off unnecessary lights during daytime operation.</p>
              <p className="mt-3 text-sm text-emerald-300">Estimated daily savings: 3.0 kWh</p>
            </div>
          </div>

          <div className="card p-5">
            <h2 className="mb-4 text-lg font-semibold">Anomalies</h2>
            <div className="space-y-3">
              {anomalies.map((item) => (
                <div key={item.zone} className="rounded-xl border border-red-500/30 bg-red-500/5 p-3">
                  <p className="font-medium">{item.zone}</p>
                  <p className="mt-1 text-sm text-red-300">Risk: {item.risk}</p>
                  <p className="mt-2 text-sm text-slate-300">{item.explanation}</p>
                </div>
              ))}
            </div>
          </div>
        </section>

        <section className="card p-5">
          <h2 className="mb-4 text-lg font-semibold">What-if Simulator</h2>
          <div className="grid gap-6 md:grid-cols-[1.2fr_0.8fr]">
            <div>
              <label className="mb-2 block text-sm text-slate-300">AC setpoint change</label>
              <input
                type="range"
                min={1}
                max={3}
                value={setpoint}
                onChange={(e) => setSetpoint(Number(e.target.value))}
                className="w-full accent-emerald-500"
              />
              <div className="mt-2 flex justify-between text-sm text-slate-400">
                <span>+1°C</span>
                <span>+{setpoint}°C</span>
                <span>+3°C</span>
              </div>
              <div className="mt-5">
                <label className="mb-2 block text-sm text-slate-300">Active time</label>
                <input value={hours} onChange={(e) => setHours(e.target.value)} className="w-full rounded-xl border border-slate-700 bg-slate-900 px-3 py-2 text-slate-100" />
              </div>
            </div>

            <div className="rounded-2xl border border-slate-700 bg-slate-800/70 p-4">
              <p className="text-sm text-slate-400">Current demand</p>
              <p className="mt-2 text-3xl font-semibold">{simulated.current.toFixed(1)} kWh</p>
              <p className="mt-4 text-sm text-slate-400">Simulated demand</p>
              <p className="mt-2 text-2xl font-semibold text-emerald-300">{simulated.simulatedDemand.toFixed(1)} kWh</p>
              <p className="mt-4 text-sm text-slate-400">Energy saved</p>
              <p className="mt-2 text-xl font-semibold text-emerald-300">{simulated.energySaved.toFixed(2)} kWh</p>
              <p className="mt-4 text-sm text-slate-400">Cost saved</p>
              <p className="mt-2 text-xl font-semibold text-amber-300">${simulated.costSaved.toFixed(2)}</p>
            </div>
          </div>
        </section>
      </div>
    </div>
  )
}

export default App
