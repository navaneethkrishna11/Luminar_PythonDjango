import React from 'react'

const Card = ({ slot, onBook }) => {
  const {
    id,
    name,
    description,
    image,
    total_slots,
    available_slots,
  } = slot

  const occupancy = total_slots > 0 ? ((total_slots - available_slots) / total_slots) * 100 : 0
  const isAvailable = available_slots > 0

  return (
    <div className="group relative flex flex-col rounded-2xl overflow-hidden border border-[#629FAD]/20 bg-white/60 backdrop-blur-md shadow-sm hover:shadow-xl hover:shadow-[#629FAD]/10 hover:-translate-y-1.5 transition-all duration-300">

      {/* Image area */}
      <div className="relative h-44 overflow-hidden bg-[#629FAD]/8">
        {image ? (
          <img
            src={image}
            alt={name}
            className="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500"
          />
        ) : (
          <div className="w-full h-full flex items-center justify-center bg-gradient-to-br from-[#629FAD]/10 to-[#629FAD]/5">
            <svg className="w-14 h-14 text-[#629FAD]/25" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={1}
                d="M8 14v3m4-3v3m4-3v3M3 21h18M3 10h18M3 7l9-4 9 4M4 10h16v11H4V10z" />
            </svg>
          </div>
        )}

        {/* Availability pill */}
        <div className={`absolute top-3 right-3 inline-flex items-center gap-1.5 px-2.5 py-1 rounded-full text-[11px] font-semibold backdrop-blur-sm border
          ${isAvailable
            ? 'bg-emerald-50/90 border-emerald-200/70 text-emerald-700'
            : 'bg-rose-50/90 border-rose-200/70 text-rose-600'}`}>
          <span className={`w-1.5 h-1.5 rounded-full animate-pulse ${isAvailable ? 'bg-emerald-500' : 'bg-rose-500'}`} />
          {isAvailable ? 'Available' : 'Fully Booked'}
        </div>

        {/* Subtle bottom fade */}
        <div className="absolute bottom-0 left-0 right-0 h-10 bg-gradient-to-t from-white/30 to-transparent" />
      </div>

      {/* Body */}
      <div className="flex flex-col flex-1 p-5 gap-4">

        {/* Title & desc */}
        <div>
          <h3 className="text-[15px] font-semibold text-slate-800 leading-snug tracking-tight">{name}</h3>
          {description && (
            <p className="mt-1.5 text-[12.5px] text-slate-500 leading-relaxed line-clamp-2">{description}</p>
          )}
        </div>

        {/* Stats row */}
        <div className="flex gap-2">
          <div className="flex-1 rounded-xl bg-[#629FAD]/8 px-3 py-2 text-center">
            <p className="text-[11px] text-slate-400 mb-0.5">Total</p>
            <p className="text-sm font-bold text-[#3d7a88]">{total_slots}</p>
          </div>
          <div className="flex-1 rounded-xl bg-emerald-50 px-3 py-2 text-center">
            <p className="text-[11px] text-slate-400 mb-0.5">Available</p>
            <p className="text-sm font-bold text-emerald-600">{available_slots}</p>
          </div>
          <div className="flex-1 rounded-xl bg-slate-50 px-3 py-2 text-center">
            <p className="text-[11px] text-slate-400 mb-0.5">Booked</p>
            <p className="text-sm font-bold text-slate-600">{total_slots - available_slots}</p>
          </div>
        </div>

        {/* Progress bar */}
        <div className="space-y-1.5">
          <div className="flex justify-between items-center">
            <span className="text-[11px] text-slate-400">Occupancy</span>
            <span className="text-[11px] font-semibold text-[#629FAD]">{Math.round(occupancy)}%</span>
          </div>
          <div className="h-1.5 rounded-full bg-[#629FAD]/12 overflow-hidden">
            <div
              className="h-full rounded-full bg-gradient-to-r from-[#629FAD] to-[#4e8a97] transition-all duration-700"
              style={{ width: `${occupancy}%` }}
            />
          </div>
        </div>

        {/* CTA */}
        <button
          disabled={!isAvailable}
          onClick={() => onBook && onBook(id)}
          className={`mt-auto w-full py-2.5 rounded-xl text-[13px] font-semibold tracking-wide transition-all duration-200
            ${isAvailable
              ? 'bg-[#42aa57] text-white hover:bg-[#8fe69e] active:scale-[0.98] shadow-sm hover:shadow-lg hover:shadow-[#629FAD]/20'
              : 'bg-slate-100 text-slate-400 cursor-not-allowed'}`}
        >
          {isAvailable ? 'Book Slot →' : 'Not Available'}
        </button>
      </div>
    </div>
  )
}

export default Card