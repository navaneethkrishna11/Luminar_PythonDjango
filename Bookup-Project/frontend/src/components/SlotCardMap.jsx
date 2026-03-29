import React, { useEffect, useState } from 'react'
import Card from './Card'
import { getallslot } from '../services/apicall'

const SlotCardMap = () => {
  const [slots, setSlots] = useState([])
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState(null)
  const [filter, setFilter] = useState('all') // all | available | full

  useEffect(() => {
    fetchSlots()
  }, [])

  const fetchSlots = async () => {
    try {
      setLoading(true)
      setError(null)
      const res = await getallslot()
      setSlots(res.data)
    } catch (err) {
      setError('Failed to load slots. Please try again.')
    } finally {
      setLoading(false)
    }
  }

  const filtered = slots.filter(s => {
    if (filter === 'available') return s.available_slots > 0
    if (filter === 'full') return s.available_slots === 0
    return true
  })

  return (
    <section className="w-full p-25">

      {/* Header row */}
      <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4 mb-8">
        <div>
          <h2 className="text-xl font-bold text-slate-800 tracking-tight">All Slots</h2>
          <p className="text-sm text-slate-500 mt-0.5">
            {loading ? 'Loading...' : `${filtered.length} slot${filtered.length !== 1 ? 's' : ''} found`}
          </p>
        </div>

        {/* Filter pills */}
        <div className="inline-flex items-center gap-1 p-1 rounded-full border border-[#629FAD]/25 bg-white/50 backdrop-blur-sm">
          {[
            { key: 'all', label: 'All' },
            { key: 'available', label: 'Available' },
            { key: 'full', label: 'Full' },
          ].map(f => (
            <button
              key={f.key}
              onClick={() => setFilter(f.key)}
              className={`px-4 py-1.5 rounded-full text-xs font-semibold transition-all duration-200
                ${filter === f.key
                  ? 'bg-[#629FAD] text-white shadow-sm'
                  : 'text-slate-500 hover:text-[#629FAD]'}`}
            >
              {f.label}
            </button>
          ))}
        </div>
      </div>

      {/* Loading skeleton */}
      {loading && (
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-5">
          {[...Array(8)].map((_, i) => (
            <div key={i} className="rounded-2xl border border-[#629FAD]/10 bg-white/50 overflow-hidden animate-pulse">
              <div className="h-44 bg-[#629FAD]/8" />
              <div className="p-5 space-y-3">
                <div className="h-4 bg-slate-200/80 rounded-lg w-3/4" />
                <div className="h-3 bg-slate-100 rounded-lg w-full" />
                <div className="h-3 bg-slate-100 rounded-lg w-2/3" />
                <div className="flex gap-2 mt-2">
                  <div className="flex-1 h-12 bg-slate-100 rounded-xl" />
                  <div className="flex-1 h-12 bg-slate-100 rounded-xl" />
                  <div className="flex-1 h-12 bg-slate-100 rounded-xl" />
                </div>
                <div className="h-10 bg-[#629FAD]/10 rounded-xl mt-2" />
              </div>
            </div>
          ))}
        </div>
      )}

      {/* Error */}
      {!loading && error && (
        <div className="flex flex-col items-center justify-center py-20 gap-4">
          <div className="w-12 h-12 rounded-full bg-rose-50 flex items-center justify-center">
            <svg className="w-5 h-5 text-rose-400" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2}
                d="M12 9v2m0 4h.01M12 3a9 9 0 100 18A9 9 0 0012 3z" />
            </svg>
          </div>
          <p className="text-sm text-slate-500">{error}</p>
          <button
            onClick={fetchSlots}
            className="px-4 py-2 rounded-xl bg-[#629FAD] text-white text-sm font-medium hover:bg-[#4e8a97] transition-colors"
          >
            Retry
          </button>
        </div>
      )}

      {/* Empty state */}
      {!loading && !error && filtered.length === 0 && (
        <div className="flex flex-col items-center justify-center py-20 gap-3">
          <div className="w-14 h-14 rounded-2xl bg-[#629FAD]/10 flex items-center justify-center">
            <svg className="w-6 h-6 text-[#629FAD]/50" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={1.5}
                d="M20 13V6a2 2 0 00-2-2H6a2 2 0 00-2 2v7m16 0v5a2 2 0 01-2 2H6a2 2 0 01-2-2v-5m16 0h-2.586a1 1 0 00-.707.293l-2.414 2.414a1 1 0 01-.707.293h-3.172a1 1 0 01-.707-.293l-2.414-2.414A1 1 0 006.586 13H4" />
            </svg>
          </div>
          <p className="text-sm text-slate-500">No slots found for this filter.</p>
        </div>
      )}

      {/* Cards grid */}
      {!loading && !error && filtered.length > 0 && (
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-5">
          {filtered.map(slot => (
            <Card
              key={slot.id}
              slot={slot}
              onBook={(id) => console.log('Book slot:', id)} // wire up your booking handler
            />
          ))}
        </div>
      )}

    </section>
  )
}

export default SlotCardMap