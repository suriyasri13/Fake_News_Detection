import React from 'react';

function App() {
  const scrollTo = (id) => {
    const element = document.getElementById(id);
    if (element) element.scrollIntoView({ behavior: 'smooth' });
  };

  return (
    <div className="min-h-screen bg-[#020617] text-white font-sans selection:bg-blue-500/30">
      {/* Background Decor */}
      <div className="fixed inset-0 overflow-hidden pointer-events-none">
        <div className="absolute -top-24 -right-24 w-96 h-96 bg-blue-600/20 blur-[120px] rounded-full"></div>
        <div className="absolute top-1/2 -left-24 w-72 h-72 bg-purple-600/10 blur-[100px] rounded-full"></div>
      </div>

      {/* Navbar */}
      <nav className="fixed top-0 w-full z-50 px-6 py-6 border-b border-white/5 bg-[#020617]/80 backdrop-blur-xl">
        <div className="max-w-7xl mx-auto flex justify-between items-center">
          <div className="flex items-center gap-2 cursor-pointer" onClick={() => window.scrollTo({top: 0, behavior: 'smooth'})}>
            <div className="w-10 h-10 bg-blue-600 rounded-lg flex items-center justify-center shadow-lg shadow-blue-500/50">
               <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="3" strokeLinecap="round" strokeLinejoin="round"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>
            </div>
            <span className="text-2xl font-black tracking-tighter uppercase">FAKE NEWS <span className="text-blue-500">DETECTION</span></span>
          </div>
          <div className="hidden md:flex gap-8 text-[10px] font-black tracking-widest text-slate-400">
            <button onClick={() => scrollTo('features')} className="hover:text-white transition-colors">FEATURES</button>
            <button onClick={() => scrollTo('tech')} className="hover:text-white transition-colors">TECHNOLOGY</button>
            <button onClick={() => scrollTo('author')} className="hover:text-white transition-colors">ABOUT</button>
          </div>
          <button 
            onClick={() => window.open('http://localhost:8501', '_blank')}
            className="px-6 py-2 bg-blue-600 hover:bg-blue-500 rounded-full text-[10px] font-black tracking-widest transition-all hover:scale-105 shadow-lg shadow-blue-500/20"
          >
            LAUNCH ENGINE
          </button>
        </div>
      </nav>

      {/* Hero Section */}
      <section className="pt-48 pb-32 px-6 relative">
        <div className="max-w-7xl mx-auto grid grid-cols-1 lg:grid-cols-2 gap-16 items-center">
          <div className="animate-in fade-in slide-in-from-left duration-1000">
            <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full border border-blue-500/30 bg-blue-500/10 text-blue-400 text-[10px] font-black tracking-widest mb-8 uppercase">
               Next-Gen AI Intelligence
            </div>
            <h1 className="text-6xl md:text-8xl font-black tracking-tighter leading-[0.9] mb-10">
              TRUTH <br/> 
              <span className="bg-gradient-to-r from-blue-400 via-purple-500 to-pink-500 bg-clip-text text-transparent">VERIFIED.</span>
            </h1>
            <p className="text-xl text-slate-400 mb-12 max-w-lg leading-relaxed">
              Empowering the digital world with state-of-the-art NLP algorithms to identify misinformation and sensationalism in real-time.
            </p>
            <div className="flex gap-6">
              <button onClick={() => window.open('http://localhost:8501', '_blank')} className="px-10 py-5 bg-white text-black font-black rounded-2xl hover:scale-105 transition-transform shadow-xl shadow-white/10">GET STARTED</button>
              <button onClick={() => scrollTo('features')} className="px-10 py-5 border border-white/10 hover:bg-white/5 font-black rounded-2xl transition-all">CORE FEATURES</button>
            </div>
          </div>

          <div className="relative animate-in zoom-in duration-1000">
            <div className="absolute inset-0 bg-blue-600/20 blur-[150px] rounded-full"></div>
            <div className="relative bg-slate-900/60 backdrop-blur-2xl p-4 rounded-[32px] border border-white/10 shadow-2xl">
               <img src="https://images.unsplash.com/photo-1550751827-4bd374c3f58b?auto=format&fit=crop&q=80&w=2070" className="rounded-2xl" alt="AI Scan" />
               <div className="absolute -bottom-6 -right-6 p-6 bg-slate-950/80 backdrop-blur-2xl rounded-3xl border border-white/20 shadow-2xl">
                  <div className="text-[10px] font-black opacity-50 uppercase tracking-widest text-blue-400 mb-1">AI Precision</div>
                  <div className="text-2xl font-black">98.4% Acc.</div>
               </div>
            </div>
          </div>
        </div>
      </section>

      {/* Features Section */}
      <section id="features" className="py-40 px-6 bg-slate-950/50">
        <div className="max-w-7xl mx-auto">
          <div className="text-center mb-24">
            <h2 className="text-5xl md:text-7xl font-black tracking-tighter mb-6">CORE CAPABILITIES</h2>
            <p className="text-slate-400 text-xl max-w-2xl mx-auto">Integrated modules designed for clinical misinformation detection.</p>
          </div>
          <div className="grid grid-cols-1 md:grid-cols-3 gap-10">
             {[
               { title: "URL SCRAPER", desc: "Instantly fetch and analyze news articles directly from any website URL." },
               { title: "SENTIMENT AI", desc: "Detect inflammatory tone and subjective bias patterns in linguistic structures." },
               { title: "REPORT EXPORT", desc: "Download professional PDF reports with detailed authenticity and bias metrics." }
             ].map((f, i) => (
               <div key={i} className="bg-slate-900/40 backdrop-blur-xl p-12 rounded-[32px] border border-white/5 hover:border-blue-500/50 transition-all duration-500 group">
                 <div className="w-16 h-16 bg-blue-600/20 rounded-2xl flex items-center justify-center text-blue-500 mb-8 group-hover:scale-110 transition-transform">
                    <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><circle cx="12" cy="12" r="10"/><path d="M12 16v-4"/><path d="M12 8h.01"/></svg>
                 </div>
                 <h3 className="text-3xl font-black mb-6">{f.title}</h3>
                 <p className="text-slate-400 text-lg leading-relaxed">{f.desc}</p>
               </div>
             ))}
          </div>
        </div>
      </section>

      {/* Tech Section */}
      <section id="tech" className="py-40 px-6">
        <div className="max-w-7xl mx-auto">
           <div className="bg-gradient-to-br from-blue-600/20 to-purple-600/20 p-16 rounded-[48px] border border-white/10 relative overflow-hidden">
              <h2 className="text-5xl font-black mb-12">TECHNOLOGY STACK</h2>
              <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-12">
                 {[
                   { title: "Random Forest", desc: "Ensemble learning for high-precision classification." },
                   { title: "TF-IDF Matrix", desc: "Advanced term-frequency weighting for text features." },
                   { title: "N-Gram Analysis", desc: "Capturing word sequences to detect deception." },
                   { title: "Sentiment Engine", desc: "Natural Language processing for emotional bias." }
                 ].map((t, i) => (
                   <div key={i} className="p-6 bg-black/20 rounded-3xl border border-white/5">
                      <h4 className="text-xl font-bold mb-2 text-blue-400">{t.title}</h4>
                      <p className="text-slate-500 text-sm">{t.desc}</p>
                   </div>
                 ))}
              </div>
           </div>
        </div>
      </section>

      {/* About Section */}
      <section id="author" className="py-40 px-6 bg-slate-950/50">
        <div className="max-w-4xl mx-auto text-center">
           <h2 className="text-5xl font-black mb-8">CREATED BY SURIYA SRI</h2>
           <p className="text-2xl text-slate-400 mb-12 leading-relaxed italic">
             "Protecting the integrity of information in the digital age through innovation and artificial intelligence."
           </p>
           <button 
             onClick={() => window.open('https://github.com/suriyasri13/Fake_News_Detection', '_blank')} 
             className="inline-flex items-center gap-3 px-10 py-5 bg-slate-900 border border-white/10 rounded-2xl hover:bg-slate-800 transition-all font-black"
           >
             <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><path d="M9 19c-5 1.5-5-2.5-7-3m14 6v-3.87a3.37 3.37 0 0 0-.94-2.61c3.14-.35 6.44-1.54 6.44-7A5.44 5.44 0 0 0 20 4.77 5.07 5.07 0 0 0 19.91 1S18.73.65 16 2.48a13.38 13.38 0 0 0-7 0C6.27.65 5.09 1 5.09 1A5.07 5.07 0 0 0 5 4.77a5.44 5.44 0 0 0-1.5 3.78c0 5.42 3.3 6.61 6.44 7A3.37 3.37 0 0 0 9 18.13V22"/></svg>
             VIEW ON GITHUB
           </button>
        </div>
      </section>

      {/* Footer */}
      <footer className="py-20 px-6 border-t border-white/5 text-center opacity-40">
        <p className="text-xs font-black tracking-[0.4em] uppercase">FAKE NEWS DETECTION | © 2026 SURIYA SRI</p>
      </footer>
    </div>
  );
}

export default App;
