import React from 'react';
import { motion } from 'framer-motion';
import { Shield, Zap, Search, Download, Activity, Cpu, Database, BarChart, Github } from 'lucide-react';

function App() {
  const scrollTo = (id) => {
    const element = document.getElementById(id);
    if (element) {
      element.scrollIntoView({ behavior: 'smooth' });
    }
  };

  return (
    <div className="min-h-screen selection:bg-blue-500/30">
      {/* Navbar */}
      <nav className="fixed top-0 w-full z-50 px-6 py-6 border-b border-white/5 bg-slate-950/80 backdrop-blur-xl">
        <div className="max-w-7xl mx-auto flex justify-between items-center">
          <div className="flex items-center gap-2 cursor-pointer" onClick={() => window.scrollTo({top: 0, behavior: 'smooth'})}>
            <Shield className="text-blue-500" size={32} />
            <span className="text-2xl font-extrabold tracking-tighter uppercase">FactGuard<span className="text-blue-500">AI</span></span>
          </div>
          <div className="hidden md:flex gap-8 text-xs font-black tracking-widest text-slate-400">
            <button onClick={() => scrollTo('features')} className="hover:text-white transition-colors">FEATURES</button>
            <button onClick={() => scrollTo('tech')} className="hover:text-white transition-colors">TECHNOLOGY</button>
            <button onClick={() => scrollTo('author')} className="hover:text-white transition-colors">ABOUT</button>
          </div>
          <button 
            onClick={() => window.open('http://localhost:8501', '_blank')}
            className="px-6 py-2 bg-blue-600 hover:bg-blue-500 rounded-full text-xs font-black tracking-widest transition-all hover:scale-105 shadow-lg shadow-blue-500/20"
          >
            LAUNCH ENGINE
          </button>
        </div>
      </nav>

      {/* Hero Section */}
      <section className="pt-48 pb-32 px-6">
        <div className="max-w-7xl mx-auto grid grid-cols-1 lg:grid-cols-2 gap-16 items-center">
          <motion.div initial={{ opacity: 0, y: 20 }} animate={{ opacity: 1, y: 0 }} transition={{ duration: 0.8 }}>
            <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full border border-blue-500/30 bg-blue-500/10 text-blue-400 text-[10px] font-black tracking-widest mb-8 uppercase">
              <Zap size={14} /> Next-Gen Intelligence
            </div>
            <h1 className="text-6xl md:text-8xl font-black tracking-tighter leading-[0.9] mb-10">
              TRUTH <br/> 
              <span className="text-gradient">ENGINEERED.</span>
            </h1>
            <p className="text-xl text-slate-400 mb-12 max-w-lg leading-relaxed">
              Detect misinformation with clinical precision. Our AI-driven platform scans the web to protect information integrity.
            </p>
            <div className="flex gap-6">
              <button onClick={() => window.open('http://localhost:8501', '_blank')} className="px-10 py-5 bg-white text-black font-black rounded-2xl hover:scale-105 transition-transform">GET STARTED</button>
              <button onClick={() => scrollTo('features')} className="px-10 py-5 border border-white/10 hover:bg-white/5 font-black rounded-2xl transition-all">CORE FEATURES</button>
            </div>
          </motion.div>

          <motion.div initial={{ opacity: 0, scale: 0.9 }} animate={{ opacity: 1, scale: 1 }} transition={{ duration: 1 }} className="relative">
            <div className="absolute inset-0 bg-blue-600/30 blur-[150px] rounded-full bg-pulse"></div>
            <div className="relative glass-card p-4 glow-shadow">
               <img src="https://images.unsplash.com/photo-1550751827-4bd374c3f58b?auto=format&fit=crop&q=80&w=2070" className="rounded-2xl" alt="AI Hub" />
               <div className="absolute -bottom-6 -right-6 p-6 glass-card border-white/20">
                  <Activity className="text-blue-400 mb-2" />
                  <div className="text-[10px] font-black opacity-50 uppercase tracking-widest">Real-time Analysis</div>
                  <div className="text-2xl font-black">98.4% Acc.</div>
               </div>
            </div>
          </motion.div>
        </div>
      </section>

      {/* Features Section */}
      <section id="features" className="py-40 px-6 bg-slate-950/50">
        <div className="max-w-7xl mx-auto">
          <div className="text-center mb-24">
            <h2 className="text-5xl md:text-7xl font-black tracking-tighter mb-6">CORE CAPABILITIES</h2>
            <p className="text-slate-400 text-xl max-w-2xl mx-auto">Three specialized modules working in harmony to verify digital content.</p>
          </div>
          <div className="grid grid-cols-1 md:grid-cols-3 gap-10">
             {[
               { icon: <Search />, title: "URL SCRAPER", desc: "Instantly fetch and analyze news articles directly from any website URL." },
               { icon: <Shield />, title: "SENTIMENT AI", desc: "Detect inflammatory tone and subjective bias patterns in linguistic structures." },
               { icon: <Download />, title: "REPORT EXPORT", desc: "Download professional PDF reports with detailed authenticity and bias metrics." }
             ].map((f, i) => (
               <motion.div key={i} whileHover={{ y: -15 }} className="glass-card p-12 border-white/5 hover:border-blue-500/50 transition-all duration-500">
                 <div className="w-16 h-16 bg-blue-600/20 rounded-3xl flex items-center justify-center text-blue-500 mb-8">{f.icon}</div>
                 <h3 className="text-3xl font-black mb-6">{f.title}</h3>
                 <p className="text-slate-400 text-lg leading-relaxed">{f.desc}</p>
               </motion.div>
             ))}
          </div>
        </div>
      </section>

      {/* Technology Section */}
      <section id="tech" className="py-40 px-6">
        <div className="max-w-7xl mx-auto">
           <div className="glass-card p-16 border-blue-500/10 overflow-hidden relative">
              <div className="absolute top-0 right-0 w-96 h-96 bg-blue-600/10 blur-[100px]"></div>
              <h2 className="text-5xl font-black mb-12">THE TECHNOLOGY STACK</h2>
              <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-12">
                 {[
                   { icon: <Cpu />, title: "Random Forest", desc: "Ensemble learning for high-precision classification." },
                   { icon: <Database />, title: "TF-IDF Vectorizer", desc: "Advanced term-frequency weighting for text features." },
                   { icon: <BarChart />, title: "N-Gram Analysis", desc: "Capturing word sequences to detect deception." },
                   { icon: <Activity />, title: "Sentiment Analysis", desc: "Natural Language processing for emotional bias." }
                 ].map((t, i) => (
                   <div key={i}>
                      <div className="text-blue-500 mb-4">{t.icon}</div>
                      <h4 className="text-xl font-bold mb-2">{t.title}</h4>
                      <p className="text-slate-500 text-sm">{t.desc}</p>
                   </div>
                 ))}
              </div>
           </div>
        </div>
      </section>

      {/* About / Author Section */}
      <section id="author" className="py-40 px-6 bg-slate-950/50">
        <div className="max-w-4xl mx-auto text-center">
           <div className="mb-12 inline-block p-4 rounded-full bg-blue-600/10 border border-blue-500/20">
              <Shield size={48} className="text-blue-500" />
           </div>
           <h2 className="text-5xl font-black mb-8">CREATED BY SURIYA SRI</h2>
           <p className="text-2xl text-slate-400 mb-12 leading-relaxed italic">
             "Information integrity is the cornerstone of a free society. This project is my contribution to a more truthful digital future."
           </p>
           <div className="flex justify-center gap-6">
              <button onClick={() => window.open('https://github.com/suriyasri13/Fake_News_Detection', '_blank')} className="flex items-center gap-2 px-8 py-4 bg-slate-900 rounded-2xl hover:bg-slate-800 transition-colors">
                <Github size={20} /> VIEW SOURCE
              </button>
           </div>
        </div>
      </section>

      {/* Footer */}
      <footer className="py-20 px-6 border-t border-white/5 text-center">
        <div className="max-w-7xl mx-auto opacity-50">
          <p className="text-xs font-black tracking-[0.3em] uppercase">FactGuard Intelligence | © 2026 Suriya Sri</p>
        </div>
      </footer>
    </div>
  );
}

export default App;
