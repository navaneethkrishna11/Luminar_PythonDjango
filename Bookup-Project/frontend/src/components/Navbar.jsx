import React, { useState, useEffect } from 'react'
import { userlogout } from '../services/apicall'

const guestLinks = ['Home', 'Services', 'About', 'Contact']
const authLinks  = ['Home', 'Dashboard']

const Navbar = () => {
  const [scrolled,   setScrolled]   = useState(false)
  const [open,       setOpen]       = useState(false)
  const [isLoggedIn, setIsLoggedIn] = useState(false)

  useEffect(() => {
    // Check token on mount
    setIsLoggedIn(!!localStorage.getItem('Token'))

    const fn = () => setScrolled(window.scrollY > 10)
    window.addEventListener('scroll', fn)
    return () => window.removeEventListener('scroll', fn)
  }, [])

  const handleLogout = async () => {
    try {
      await userlogout()
    } catch (_) {
      // proceed even if API call fails
    } finally {
      localStorage.removeItem('Token')
      setIsLoggedIn(false)
      window.location.href = '/'
    }
  }

  const links = isLoggedIn ? authLinks : guestLinks

  const linkHref = (l) => {
    if (l === 'Home')      return '/'
    if (l === 'Dashboard') return '/dashboard'
    return `/${l.toLowerCase()}`
  }

  return (
    <header className="fixed top-0 left-0 right-0 z-50 flex justify-center pt-4 px-4">
      <nav className={`w-full max-w-3xl flex items-center justify-between px-5 py-2.5 rounded-full transition-all duration-300 ${
        scrolled
          ? 'bg-white/95 backdrop-blur-lg shadow-[0_4px_24px_rgba(98,159,173,0.12)] border border-[#629FAD]/20'
          : 'bg-white/75 backdrop-blur-md border border-[#629FAD]/15'
      }`}>

        {/* Logo */}
        <a href="/" style={{ textDecoration: 'none' }}
          className="font-['Cormorant_Garamond'] text-xl font-bold text-[#2a6474] leading-none">
          Book<span className="text-[#629FAD]">Up</span>
        </a>

        {/* Desktop links */}
        <ul className="hidden md:flex items-center gap-0.5 list-none m-0 p-0">
          {links.map(l => (
            <li key={l}>
              <a
                href={linkHref(l)}
                style={{ textDecoration: 'none' }}
                className="px-3.5 py-1.5 rounded-full text-[0.82rem] font-medium text-[#629FAD] hover:text-[#2a6474] hover:bg-[#629FAD]/8 transition-all duration-200"
              >
                {l}
              </a>
            </li>
          ))}
        </ul>

        {/* Desktop auth */}
        <div className="hidden md:flex items-center gap-1.5">
          {isLoggedIn ? (
            <button
              onClick={handleLogout}
              className="text-[0.82rem] font-semibold text-[#629FAD] border border-[#629FAD]/40 px-4 py-1.5 rounded-full hover:bg-[#629FAD] hover:text-white transition-all duration-200"
            >
              Logout
            </button>
          ) : (
            <a
              href="/auth"
              style={{ textDecoration: 'none' }}
              className="text-[0.82rem] font-semibold bg-[#629FAD] text-white px-4 py-1.5 rounded-full hover:bg-[#4e8a97] transition-all shadow-sm hover:shadow-md hover:shadow-[#629FAD]/20"
            >
              Sign up
            </a>
          )}
        </div>

        {/* Hamburger */}
        <button
          onClick={() => setOpen(!open)}
          className="md:hidden flex flex-col justify-center items-center gap-[5px] w-8 h-8 rounded-full hover:bg-[#629FAD]/10 transition-all"
        >
          <span className={`block h-px w-4 bg-[#629FAD] transition-all duration-200 ${open ? 'rotate-45 translate-y-[6px]' : ''}`} />
          <span className={`block h-px w-4 bg-[#629FAD] transition-all duration-200 ${open ? 'opacity-0' : ''}`} />
          <span className={`block h-px w-4 bg-[#629FAD] transition-all duration-200 ${open ? '-rotate-45 -translate-y-[6px]' : ''}`} />
        </button>
      </nav>

      {/* Mobile dropdown */}
      {open && (
        <div className="absolute top-[68px] left-4 right-4 bg-white/95 backdrop-blur-md rounded-2xl border border-[#629FAD]/20 shadow-[0_8px_32px_rgba(98,159,173,0.14)] p-3 md:hidden">
          {links.map(l => (
            <a
              key={l}
              href={linkHref(l)}
              style={{ textDecoration: 'none' }}
              className="block px-3 py-2.5 rounded-xl text-sm font-medium text-[#629FAD] hover:text-[#2a6474] hover:bg-[#629FAD]/8 transition-all"
            >
              {l}
            </a>
          ))}

          <div className="mt-2 pt-2 border-t border-[#629FAD]/15 flex gap-2">
            {isLoggedIn ? (
              <button
                onClick={handleLogout}
                className="flex-1 text-center text-sm font-semibold border border-[#629FAD]/40 text-[#629FAD] py-2 rounded-xl hover:bg-[#629FAD] hover:text-white transition-all"
              >
                Logout
              </button>
            ) : (
              <a
                href="/auth"
                style={{ textDecoration: 'none' }}
                className="flex-1 text-center text-sm font-semibold bg-[#629FAD] text-white py-2 rounded-xl hover:bg-[#4e8a97] transition-all"
              >
                Sign up
              </a>
            )}
          </div>
        </div>
      )}
    </header>
  )
}

export default Navbar