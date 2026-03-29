import React, { useState, useEffect,useContext } from 'react'
import { useNavigate } from 'react-router-dom'
import { AuthContext } from '../../context/AuthContext'
import { addservice,getCurrentUser } from '../../services/apicall'

export default function Add({ onClose }) {
  const { auth } = useContext(AuthContext)
  const navigate = useNavigate()
  const [username, setUsername] = useState("");
  console.log(username)



  const [form, setForm] = useState({
    name: '', place: '', image: null,
    total_slots: '', available_slots: '', provider: username
  })

  const set = e => setForm(p => ({ ...p, [e.target.name]: e.target.value }))

  const handleSubmit = async e => {
    e.preventDefault()
      const finalData = {
    ...form,
    provider: username
  };
    // console.log(finalData)
    await addservice(finalData)
    onClose()
    navigate('/service')
  }

  useEffect(() => {
  (async () => {
    const res = await getCurrentUser();
    setUsername(res.data.id); // ✅ fix here
  })();
}, []);

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center px-4 bg-[#0C2C55]/30 backdrop-blur-sm">
      <div className="w-full max-w-md bg-white rounded-2xl shadow-xl overflow-hidden">

        {/* Header */}
        <div className="flex items-center justify-between px-6 py-4 border-b border-slate-100">
          <h2 className="font-['Cormorant_Garamond'] text-lg font-bold text-[#0C2C55]">Add Service</h2>
          <button onClick={onClose} className="text-slate-400 hover:text-slate-600 text-xl leading-none transition-colors">✕</button>
        </div>

        {/* Form */}
        <form onSubmit={handleSubmit} className="px-6 py-5 space-y-4">

          {[['Name', 'name', 'text', 'Service name'], ['Place', 'place', 'text', 'City / Location']].map(([label, name, type, ph]) => (
            <div key={name}>
              <label className="block text-xs font-semibold text-slate-500 mb-1.5">{label}</label>
              <input name={name} type={type} placeholder={ph} value={form[name]} onChange={set} required
                className="w-full px-4 py-2.5 rounded-xl border border-slate-200 text-sm text-[#0C2C55] placeholder:text-slate-300 outline-none focus:border-[#629FAD] focus:shadow-[0_0_0_3px_rgba(98,159,173,0.10)] transition-all" />
            </div>
          ))}

          {/* Image */}
          <div>
            <label className="block text-xs font-semibold text-slate-500 mb-1.5">Image</label>
            <label className="flex items-center gap-3 px-4 py-2.5 rounded-xl border border-dashed border-slate-200 hover:border-[#629FAD] cursor-pointer transition-all">
              <span className="text-base">🖼️</span>
              <span className="text-sm text-slate-400">{form.image ? form.image.name : 'Click to upload'}</span>
              <input type="file" accept="image/*" className="hidden"
                onChange={e => setForm(p => ({ ...p, image: e.target.files[0] }))} />
            </label>
          </div>

          {/* Slots */}
          <div className="grid grid-cols-2 gap-3">
            {[['Total Slots', 'total_slots'], ['Available Slots', 'available_slots']].map(([label, name]) => (
              <div key={name}>
                <label className="block text-xs font-semibold text-slate-500 mb-1.5">{label}</label>
                <input name={name} type="number" min="0" placeholder="0" value={form[name]} onChange={set} required
                  className="w-full px-4 py-2.5 rounded-xl border border-slate-200 text-sm text-[#0C2C55] outline-none focus:border-[#629FAD] focus:shadow-[0_0_0_3px_rgba(98,159,173,0.10)] transition-all" />
              </div>
            ))}
          </div>

          {/* Actions */}
          <div className="flex gap-3 pt-1">
            <button type="button" onClick={onClose}
              className="flex-1 py-2.5 rounded-xl border border-slate-200 text-sm font-medium text-slate-500 hover:bg-slate-50 transition-all">
              Cancel
            </button>
            <button type="submit"
              className="flex-1 py-2.5 rounded-xl bg-[#0C2C55] hover:bg-[#1a3d6e] text-white text-sm font-semibold transition-all shadow-sm">
              Add Service →
            </button>
          </div>

        </form>
      </div>
    </div>
  )
}


