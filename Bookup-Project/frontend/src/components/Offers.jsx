import React, { useState, useEffect } from 'react'

const steps = [
  { n: '1st', label: 'Book any service', icon: '🗓️' },
  { n: '2nd', label: 'Book a 2nd service', icon: '✂️' },
  { n: '3rd', label: 'Book a 3rd service', icon: '🩺' },
  { n: '4th', label: '100% OFF', icon: '🎁', highlight: true },
]

const badges = ['Salon', 'Doctor', 'Hotel', 'Spa', 'Gym', 'Restaurant']

export default function Offer() {
  const [count, setCount] = useState(0)

  useEffect(() => {
    const t = setInterval(() => setCount(p => (p < 847 ? p + 7 : 847)), 12)
    return () => clearInterval(t)
  }, [])

  return (
    <section className="px-6 py-24 max-w-6xl mx-auto">

      {/* Label */}
      <div className="flex items-center gap-3 mb-14">
        <span className="h-px w-12 bg-[#629FAD]/40" />
        <p className="text-[#629FAD] text-xs font-semibold tracking-[0.18em] uppercase">Limited offer</p>
      </div>

      <div className="rounded-3xl bg-[#0C2C55] overflow-hidden relative">

        {/* Glow orbs */}
        <div className="absolute inset-0 pointer-events-none">
          <div className="absolute top-0 left-1/2 -translate-x-1/2 w-[600px] h-[300px] rounded-full opacity-15"
            style={{ background: 'radial-gradient(ellipse, #629FAD 0%, transparent 70%)' }} />
          <div className="absolute bottom-0 right-0 w-72 h-72 rounded-full opacity-10"
            style={{ background: 'radial-gradient(circle, #629FAD 0%, transparent 70%)' }} />
        </div>

        <div className="relative z-10 p-10 md:p-14">

          {/* Headline */}
          <div className="text-center mb-12">
            <span className="inline-block px-4 py-1.5 rounded-full bg-[#629FAD]/20 border border-[#629FAD]/30 text-[#629FAD] text-xs font-bold tracking-widest uppercase mb-5">
              Book More · Save More
            </span>
            <h2 className="font-['Cormorant_Garamond'] text-white font-bold leading-tight mb-3"
              style={{ fontSize: 'clamp(2.2rem, 5vw, 3.8rem)' }}>
              Book 3 services.<br />
              <em className="italic text-[#629FAD]">Your 4th is on us.</em>
            </h2>
            <p className="text-white/50 text-sm max-w-md mx-auto">
              Stack your bookings in a single day — we'll cover the 4th one completely. No catch.
            </p>
          </div>

          {/* Steps */}
          <div className="grid grid-cols-2 md:grid-cols-4 gap-4 mb-12">
            {steps.map(({ n, label, icon, highlight }) => (
              <div key={n}
                className={`relative flex flex-col items-center text-center p-6 rounded-2xl border transition-all ${
                  highlight
                    ? 'bg-[#629FAD] border-[#629FAD] shadow-[0_0_40px_rgba(98,159,173,0.4)]'
                    : 'bg-white/05 border-white/10'
                }`}>
                {/* Connector dot — hide on last */}
                {!highlight && (
                  <span className="absolute -right-2.5 top-1/2 -translate-y-1/2 w-5 h-0.5 bg-white/15 hidden md:block" />
                )}
                <span className="text-2xl mb-3">{icon}</span>
                <span className={`text-xs font-bold tracking-wider uppercase mb-1 ${highlight ? 'text-white' : 'text-white/40'}`}>{n}</span>
                <span className={`text-sm font-semibold ${highlight ? 'text-white' : 'text-white/70'}`}>{label}</span>
                {highlight && (
                  <span className="mt-2 text-white text-xs font-medium bg-white/20 px-3 py-1 rounded-full">Free booking</span>
                )}
              </div>
            ))}
          </div>

          {/* Bottom row */}
          <div className="flex flex-col md:flex-row items-center justify-between gap-6 pt-8 border-t border-white/10">

            {/* Live counter */}
            <div className="flex items-center gap-3">
              <div className="flex -space-x-2">
                {['#8BBBC5','#629FAD','#4a8fa0'].map((c,i) => (
                  <div key={i} className="w-7 h-7 rounded-full border-2 border-[#0C2C55]" style={{ background: c }} />
                ))}
              </div>
              <p className="text-white/60 text-sm">
                <span className="text-white font-semibold">{count}+</span> people used this offer today
              </p>
            </div>

            {/* Valid services */}
            <div className="flex flex-wrap justify-center gap-2">
              {badges.map(b => (
                <span key={b} className="text-xs text-white/60 px-3 py-1 rounded-full border border-white/10 bg-white/05">
                  {b}
                </span>
              ))}
            </div>

            {/* CTA */}
            <a href="#" style={{ textDecoration: 'none' }}
              className="shrink-0 inline-flex items-center gap-2 bg-white text-[#0C2C55] text-sm font-bold px-7 py-3 rounded-full hover:-translate-y-0.5 hover:shadow-xl transition-all shadow-lg whitespace-nowrap">
              Claim Offer →
            </a>
          </div>

        </div>
      </div>

    </section>
  )
}