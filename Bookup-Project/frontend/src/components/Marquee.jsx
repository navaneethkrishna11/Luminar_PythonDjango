import React from 'react'

const items = [
  '✦ Free cancellation on all bookings',
  '⭑ 1,200+ verified providers',
  '✦ Instant confirmation guaranteed',
  '⭑ Doctor appointments in under 2 mins',
  '✦ Exclusive weekend spa deals',
  '⭑ No booking fees — ever',
  '✦ 50,000+ happy customers',
  '⭑ Hotels from ₹499/night',
  '✦ Same-day salon slots available',
  '⭑ 4.9 star average rating',
]

export default function Marquee() {
  return (
    <div className="px-6 py-2 max-w-6xl mx-auto">
      <div className="rounded-full border border-[#629FAD]/25 bg-white/60 backdrop-blur-sm overflow-hidden py-3 shadow-sm">

        <style>{`
          .marquee-track {
            display: flex;
            width: max-content;
            animation: scroll 28s linear infinite;
          }
          .marquee-track:hover { animation-play-state: paused; }
          @keyframes scroll {
            from { transform: translateX(0); }
            to   { transform: translateX(-50%); }
          }
        `}</style>

        <div className="marquee-track select-none">
          {[...items, ...items].map((item, i) => (
            <span key={i} className="flex items-center gap-6 px-6 text-[0.78rem] font-medium text-[#296374] whitespace-nowrap">
              {item}
            </span>
          ))}
        </div>

      </div>
    </div>
  )
}