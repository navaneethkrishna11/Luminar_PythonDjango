import React from 'react'

const problems = [
  { icon: '📱', text: 'Switching 5 different apps just to book basic services' },
  { icon: '⏳', text: 'Waiting on hold or visiting in person to check availability' },
  { icon: '😤', text: 'No way to compare providers, prices, or reviews in one place' },
  { icon: '🗓️', text: 'Double bookings, no reminders, zero follow-up' },
]

const solutions = [
  { icon: '✦', text: 'Every service — one search, one platform' },
  { icon: '✦', text: 'Real-time availability, instant confirmation' },
  { icon: '✦', text: 'Compare verified providers side by side' },
  { icon: '✦', text: 'Smart reminders & booking history, always synced' },
]

export default function Banner() {
  return (
    <section className="px-6 py-24 max-w-6xl mx-auto">

      {/* Section label */}
      <div className="flex items-center gap-3 mb-14">
        <span className="h-px flex-1 max-w-[48px] bg-[#629FAD]/40" />
        <p className="text-[#629FAD] text-xs font-semibold tracking-[0.18em] uppercase">Why BookUp exists</p>
      </div>

      <div className="grid md:grid-cols-2 gap-6 items-stretch">

        {/* Problem card */}
        <div className="rounded-3xl bg-white/50 border border-slate-200/70 p-8 backdrop-blur-sm">
          <span className="inline-block text-xs font-bold tracking-widest uppercase text-slate-400 mb-6">The Problem</span>
          <h2 className="font-['Cormorant_Garamond'] text-[#0C2C55] font-bold leading-tight mb-8"
            style={{ fontSize: 'clamp(1.8rem, 3.5vw, 2.6rem)' }}>
            Booking anything is still<br />
            <em className="italic text-slate-400">painfully scattered.</em>
          </h2>
          <ul className="space-y-4">
            {problems.map(({ icon, text }) => (
              <li key={text} className="flex items-start gap-3">
                <span className="mt-0.5 text-base shrink-0">{icon}</span>
                <p className="text-slate-500 text-sm leading-relaxed">{text}</p>
              </li>
            ))}
          </ul>
        </div>

        {/* Solution card */}
        <div className="rounded-3xl bg-[#0C2C55] border border-[#1a3d6e] p-8 relative overflow-hidden">
          {/* Subtle glow */}
          <div className="absolute top-0 right-0 w-64 h-64 rounded-full opacity-20 pointer-events-none"
            style={{ background: 'radial-gradient(circle, #629FAD 0%, transparent 70%)', transform: 'translate(30%, -30%)' }} />

          <span className="inline-block text-xs font-bold tracking-widest uppercase text-[#629FAD]/70 mb-6">The Solution</span>
          <h2 className="font-['Cormorant_Garamond'] text-white font-bold leading-tight mb-8"
            style={{ fontSize: 'clamp(1.8rem, 3.5vw, 2.6rem)' }}>
            One place for<br />
            <em className="italic text-[#629FAD]">every booking.</em>
          </h2>
          <ul className="space-y-4">
            {solutions.map(({ icon, text }) => (
              <li key={text} className="flex items-start gap-3">
                <span className="mt-1 text-[#629FAD] text-xs shrink-0">{icon}</span>
                <p className="text-white/75 text-sm leading-relaxed">{text}</p>
              </li>
            ))}
          </ul>

          <div className="mt-10">
            <a href="#" style={{ textDecoration: 'none' }}
              className="inline-flex items-center gap-2 bg-[#629FAD] hover:bg-[#7ab3bf] text-white text-sm font-semibold px-6 py-3 rounded-full transition-all hover:-translate-y-px shadow-lg">
              Get started free
              <span>→</span>
            </a>
          </div>
        </div>

      </div>

      {/* Bottom connector — bridge statement */}
      <p className="text-center text-slate-400 text-sm mt-12 max-w-md mx-auto leading-relaxed">
        Built for people who value their time —<br />
        <span className="text-[#296374] font-medium">no more app-switching, no more guessing.</span>
      </p>

    </section>
  )
}