import React, { useState } from 'react'
import Add from './Add'
import Myservice from './MyService'

const navItems = ['Dashboard', 'My Services', 'Bookings', 'Reviews', 'Settings']

export default function Service() {
  const [showAdd, setShowAdd] = useState(false)
  const [active, setActive] = useState('My Services')

  return (
    <div className="min-h-screen flex ">
      <div className="flex-1 flex flex-col min-h-screen overflow-hidden">

        {/* Topbar */}
        <header className="bg-white border-b border-slate-200/70 px-6 py-4 flex items-center justify-between shrink-0">
          <div className='mt-40'>
            <h1 className="font-['Cormorant_Garamond'] text-xl font-bold text-[#0C2C55]">{active}</h1>
            <p className="text-xs text-slate-400 mt-0.5">Manage your services and bookings</p>
          </div>
          <button onClick={() => setShowAdd(true)}
            className="flex items-center gap-2 bg-[#0C2C55] hover:bg-[#1a3d6e] text-white text-sm font-semibold px-5 py-2.5 rounded-full transition-all hover:-translate-y-px shadow-sm">
            <span className="text-base leading-none">+</span> Add Service
          </button>
        </header>

        {/* Content area — add future components here */}
        <main className="flex-1 p-6 overflow-y-auto">

          {/* Stats row — placeholder for future analytics */}
          <div className="grid grid-cols-2 md:grid-cols-4 gap-4 mb-6">
            {[['Total Services', '—'], ['Active Bookings', '—'], ['Reviews', '—'], ['Earnings', '—']].map(([label, val]) => (
              <div key={label} className="bg-white rounded-2xl border border-slate-200/70 px-5 py-4">
                <p className="text-xs text-slate-400 mb-1">{label}</p>
                <p className="font-['Cormorant_Garamond'] text-2xl font-bold text-[#0C2C55]">{val}</p>
              </div>
            ))}
          </div>

          {/* My Services section */}
          <div className="bg-white rounded-2xl border border-slate-200/70 p-5">
            <div className="flex items-center justify-between mb-5">
              <h2 className="text-sm font-semibold text-[#0C2C55]">My Services</h2>
              <span className="text-xs text-slate-400">All your listed services</span>
            </div>

            {/* MyService component renders here */}
            <Myservice/>

            {/* Future components slot in below naturally */}
          </div>

        </main>
      </div>

      {/* Add modal */}
      {showAdd && <Add onClose={() => setShowAdd(false)} />}
    </div>
  )
}