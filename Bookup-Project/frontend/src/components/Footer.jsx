import React from 'react'

const cols = [
  {
    title: 'Services',
    links: ['Doctor', 'Salon & Beauty', 'Hotels', 'Restaurant', 'Spa & Wellness', 'Gym & Fitness'],
  },
  {
    title: 'Company',
    links: ['About Us', 'How it Works', 'Careers', 'Press', 'Contact'],
  },
  {
    title: 'Support',
    links: ['Help Center', 'Privacy Policy', 'Terms of Use', 'Refund Policy'],
  },
]

export default function Footer() {
  return (
    <footer className="px-6 pt-16 pb-8 mt-8 border-t border-slate-200/60">
      <div className="max-w-6xl mx-auto">

        {/* Top */}
        <div className="grid grid-cols-2 md:grid-cols-4 gap-10 mb-14">

          {/* Brand */}
          <div className="col-span-2 md:col-span-1">
            <a href="/" style={{ textDecoration: 'none' }}
              className="font-['Cormorant_Garamond'] text-2xl font-bold text-black leading-none block mb-3">
              Book<span className="text-[#629FAD]">Up</span>
            </a>
            <p className="text-slate-400 text-sm leading-relaxed max-w-[200px]">
              Every service. One platform. Book anything in seconds.
            </p>
            {/* Socials */}
            <div className="flex gap-2 mt-5">
              {['𝕏', 'in', 'f'].map(s => (
                <a key={s} href="#" style={{ textDecoration: 'none' }}
                  className="w-8 h-8 rounded-full border border-slate-200 flex items-center justify-center text-xs text-black hover:border-[#629FAD] hover:text-[#629FAD] transition-all">
                  {s}
                </a>
              ))}
            </div>
          </div>

          {/* Link columns */}
          {cols.map(({ title, links }) => (
            <div key={title}>
              <p className="text-[0.72rem] font-bold tracking-[0.14em] uppercase text-slate-400 mb-4">{title}</p>
              <ul className="space-y-2.5 list-none">
                {links.map(l => (
                  <li key={l}>
                    <a href="#" style={{ textDecoration: 'none' }}
                      className="text-sm text-black hover:text-[#0C2C55] transition-colors">
                      {l}
                    </a>
                  </li>
                ))}
              </ul>
            </div>
          ))}
        </div>

        {/* Bottom */}
        <div className="pt-6 border-t border-slate-100 flex flex-col sm:flex-row items-center justify-between gap-3">
          <p className="text-xs text-slate-400">© 2025 BookUp. All rights reserved.</p>
          <p className="text-xs text-slate-400">
            Made with <span className="text-[#629FAD]">♥</span> for people who value their time.
          </p>
        </div>

      </div>
    </footer>
  )
}