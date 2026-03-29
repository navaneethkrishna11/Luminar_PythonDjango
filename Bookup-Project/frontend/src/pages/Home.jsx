import React from 'react'
import Navbar from '../components/Navbar'
import Hero from '../components/Hero'
import Banner from '../components/Banner'
import Marquee from '../components/Marquee'
import Offer from '../components/offers'

const Home = () => {
  return (
    <div>
      <Hero/>
      <Marquee/>
      <Banner/>
      <Offer/>

    </div>
  )
}

export default Home
