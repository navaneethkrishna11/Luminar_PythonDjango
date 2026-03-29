import React, { useState, useEffect } from 'react'

const services = [
  { label: 'Doctor',     icon: '🩺' },
  { label: 'Salon',      icon: '✂️' },
  { label: 'Hotel',      icon: '🏨' },
  { label: 'Restaurant', icon: '🍽️' },
  { label: 'Spa',        icon: '🧖' },
  { label: 'Gym',        icon: '🏋️' },
  { label: 'Lawyer',     icon: '⚖️' },
  { label: 'Tutor',      icon: '📚' },
]

const words = ['Doctor', 'Salon', 'Hotel', 'Spa', 'Anything']

export default function Hero() {
  const [word, setWord] = useState(0)
  const [fade, setFade] = useState(true)

  useEffect(() => {
    const t = setInterval(() => {
      setFade(false)
      setTimeout(() => { setWord(p => (p + 1) % words.length); setFade(true) }, 300)
    }, 2200)
    return () => clearInterval(t)
  }, [])

  return (
    <section className="min-h-screen flex flex-col justify-center px-6 pt-32 pb-20 max-w-6xl mx-auto">

      {/* Eyebrow */}
      <div className="anim d1 inline-flex items-center gap-2 self-start mb-8 px-4 py-1.5 rounded-full border border-[#629FAD]/30 bg-white/50 backdrop-blur-sm">
        <span className="w-1.5 h-1.5 rounded-full bg-[#629FAD] animate-pulse" />
        <span className="text-[#629FAD] text-xs font-semibold tracking-[0.16em] uppercase">One platform · Every service</span>
      </div>

      {/* Headline with animated word swap */}
      <h1
        className="anim d2 font-['Cormorant_Garamond'] text-[#0C2C55] font-bold leading-[1.02] tracking-tight mb-6"
        style={{ fontSize: 'clamp(3.2rem, 8vw, 6.4rem)' }}
      >
        Book a{' '}
        <span
          className="italic text-[#296374] transition-opacity duration-300"
          style={{ opacity: fade ? 1 : 0 }}
        >
          {words[word]}
        </span>
        <br />
        in 30 seconds.
      </h1>

      {/* Subtitle */}
      <p
        className="anim d3 text-[#296374] font-light leading-relaxed mb-10 max-w-lg"
        style={{ fontSize: 'clamp(1rem, 2vw, 1.15rem)' }}
      >
        Doctors, salons, hotels, tutors — every service you need, all in one place. Discover, compare, and confirm in moments.
      </p>

      {/* Search bar */}
      <div className="anim d4 flex flex-col sm:flex-row gap-3 max-w-2xl mb-12">
        <div className="flex-1 flex items-center gap-3 bg-white/90 border border-[#629FAD]/25 rounded-2xl px-5 py-4 shadow-lg focus-within:border-[#629FAD] focus-within:shadow-[0_0_0_4px_rgba(98,159,173,0.10)] transition-all">
          <svg className="w-4 h-4 text-[#629FAD] shrink-0" fill="none" stroke="currentColor" strokeWidth="2" viewBox="0 0 24 24">
            <circle cx="11" cy="11" r="8"/><path d="m21 21-4.35-4.35"/>
          </svg>
          <input
            className="flex-1 bg-transparent text-sm font-medium text-[#0C2C55] placeholder:text-[#0C2C55]/35 outline-none"
            placeholder="What are you looking for?"
          />
          <svg className="w-4 h-4 text-[#629FAD]/50 shrink-0" fill="none" stroke="currentColor" strokeWidth="2" viewBox="0 0 24 24">
            <path d="M12 2C8.13 2 5 5.13 5 9c0 5.25 7 13 7 13s7-7.75 7-13c0-3.87-3.13-7-7-7z"/><circle cx="12" cy="9" r="2.5"/>
          </svg>
        </div>
        <button className="bg-[#0C2C55] text-[#EDEDCE] text-sm font-semibold px-8 py-4 rounded-2xl shadow-lg hover:bg-[#1a3d6e] hover:-translate-y-0.5 hover:shadow-xl transition-all whitespace-nowrap">
          Find &amp; Book →
        </button>
      </div>

      {/* Service icon grid */}
      <div className="anim d5 grid grid-cols-4 sm:grid-cols-8 gap-2 mb-14">
        {services.map(({ label, icon }) => (
          <button
            key={label}
            className="group flex flex-col items-center gap-1.5 p-3 rounded-2xl bg-white/60 border border-[#629FAD]/15 hover:bg-white hover:border-[#629FAD]/40 hover:-translate-y-1 hover:shadow-lg transition-all duration-200"
          >
            <span className="text-xl group-hover:scale-110 transition-transform duration-200">{icon}</span>
            <span className="text-[#0C2C55] text-[0.67rem] font-semibold tracking-wide">{label}</span>
          </button>
        ))}
      </div>

      {/* Trust bar */}
      <div className="flex flex-wrap items-center gap-x-10 gap-y-4 pt-7 border-t border-[#0C2C55]/08">
        {[['50K+','Bookings'], ['1,200+','Providers'], ['4.9 ★','Rating'], ['12','Categories']].map(([n, l]) => (
          <div key={l} className="flex items-baseline gap-2">
            <span className="font-['Cormorant_Garamond'] text-[2rem] font-bold text-[#0C2C55] leading-none">{n}</span>
            <span className="text-[#629FAD] text-xs font-medium">{l}</span>
          </div>
        ))}
        <div className="ml-auto hidden md:flex items-center gap-3 bg-white/70 border border-[#629FAD]/18 rounded-2xl px-4 py-2.5">
          <div className="flex -space-x-2">
            {['#8BBBC5','#629FAD','#296374','#0C2C55'].map((c, i) => (
              <div key={i} className="w-7 h-7 rounded-full border-2 border-white" style={{ background: c }} />
            ))}
          </div>
          <p className="text-[#0C2C55] text-xs font-medium">
            Loved by <span className="font-semibold text-[#296374]">50,000+</span> users
          </p>
        </div>
      </div>

    </section>
  )
}