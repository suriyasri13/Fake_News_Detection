import React from 'react';
import { motion } from 'framer-motion';
import { Shield, Zap, Search, Download, ExternalLink, Activity } from 'lucide-react';

function App() {
  return (
    <div className="min-h-screen selection:bg-blue-500/30">
      {/* Navbar */}
      <nav className="fixed top-0 w-full z-50 px-6 py-6 border-b border-white/5 bg-slate-950/50 backdrop-blur-xl">
        <div className="max-w-7xl mx-auto flex justify-between items-center">
          <div className="flex items-center gap-2">
            <Shield className="text-blue-500" size={32} />
            <span className="text-2xl font-extrabold tracking-tighter">FACTGUARD<span className="text-blue-500">AI</span></span>
          </div>
          <div className="hidden md:flex gap-8 text-sm font-semibold text-slate-400">
            <a href="#features" className="hover:text-white transition-colors">FEATURES</a>
            <a href="#tech" className="hover:text-white transition-colors">TECHNOLOGY</a>
            <a href="#author" className="hover:text-white transition-colors">ABOUT</a>
          </div>
          <button 
            onClick={() => window.open('http://localhost:8501', '_blank')}
            className="px-5 py-2 bg-blue-600 hover:bg-blue-500 rounded-full text-sm font-bold transition-all hover:scale-105"
          >
            LAUNCH ENGINE
          </button>
        </div>
      </nav>

      {/* Hero Section */}
      <section className="pt-32 pb-20 px-6 overflow-hidden">
        <div className="max-w-7xl mx-auto grid grid-cols-1 lg:grid-cols-2 gap-12 items-center">
          <motion.div 
            initial={{ opacity: 0, x: -50 }}
            animate={{ opacity: 1, x: 0 }}
            transition={{ duration: 0.8 }}
          >
            <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full border border-blue-500/30 bg-blue-500/10 text-blue-400 text-xs font-bold mb-6">
              <Zap size={14} /> NEXT-GEN INFORMATION INTEGRITY
            </div>
            <h1 className="text-6xl md:text-8xl font-extrabold tracking-tighter leading-none mb-8">
              DETECT <br/> 
              <span className="text-gradient">FAKE NEWS</span> <br/>
              WITH AI.
            </h1>
            <p className="text-xl text-slate-400 mb-10 max-w-lg leading-relaxed">
              Empowering the digital world with state-of-the-art NLP algorithms to identify misinformation, sensationalism, and propaganda in real-time.
            </p>
            <div className="flex gap-4">
              <button 
                 onClick={() => window.open('http://localhost:8501', '_blank')}
                 className="px-8 py-4 bg-white text-black font-extrabold rounded-2xl hover:scale-105 transition-transform"
              >
                GET STARTED
              </button>
              <button className="px-8 py-4 border border-white/10 hover:bg-white/5 font-extrabold rounded-2xl transition-all">
                LEARN MORE
              </button>
            </div>
          </motion.div>

          <motion.div 
            initial={{ opacity: 0, scale: 0.8 }}
            animate={{ opacity: 1, scale: 1 }}
            transition={{ duration: 1 }}
            className="relative"
          >
            <div className="absolute inset-0 bg-blue-600/20 blur-[120px] rounded-full bg-pulse"></div>
            <div className="relative glass-card p-4 border border-white/10 glow-shadow overflow-hidden group">
               <img 
                 src="https://images.unsplash.com/photo-1550751827-4bd374c3f58b?auto=format&fit=crop&q=80&w=2070" 
                 alt="AI Visualization" 
                 className="rounded-xl w-full group-hover:scale-110 transition-transform duration-1000"
               />
               <div className="absolute top-8 left-8 p-4 glass-card border-white/20">
                  <Activity className="text-blue-400 mb-2" />
                  <div className="text-xs font-bold opacity-50 uppercase">Neural Scanning</div>
                  <div className="text-xl font-black">98.4% Accuracy</div>
               </div>
            </div>
          </motion.div>
        </div>
      </section>

      {/* Features Section */}
      <section id="features" className="py-32 px-6 bg-slate-950">
        <div className="max-w-7xl mx-auto">
          <div className="text-center mb-20">
            <h2 className="text-4xl md:text-6xl font-black tracking-tight mb-4">ENGINEERED FOR EXCELLENCE</h2>
            <p className="text-slate-400 text-lg">Powerful modules integrated into a single information hub.</p>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
             {[
               { icon: <Search />, title: "URL SCRAPER", desc: "Instantly fetch and analyze news articles directly from any website URL." },
               { icon: <Shield />, title: "SENTIMENT ANALYSIS", desc: "Detect inflammatory tone and subjective bias patterns in linguistic structures." },
               { icon: <Download />, title: "REPORT EXPORT", desc: "Download professional PDF reports with detailed authenticity and bias metrics." }
             ].map((f, i) => (
               <motion.div 
                 key={i}
                 whileHover={{ y: -10 }}
                 className="glass-card p-10 border-white/5 hover:border-blue-500/50 transition-colors"
               >
                 <div className="w-14 h-14 bg-blue-600/20 rounded-2xl flex items-center justify-center text-blue-500 mb-6">
                   {f.icon}
                 </div>
                 <h3 className="text-2xl font-bold mb-4">{f.title}</h3>
                 <p className="text-slate-400 leading-relaxed">{f.desc}</p>
               </motion.div>
             ))}
          </div>
        </div>
      </section>

      {/* Footer */}
      <footer className="py-20 px-6 border-t border-white/5 text-center">
        <div className="max-w-7xl mx-auto">
          <div className="flex justify-center items-center gap-2 mb-8">
            <Shield className="text-blue-500" size={32} />
            <span className="text-2xl font-extrabold tracking-tighter">FACTGUARD<span className="text-blue-500">AI</span></span>
          </div>
          <p className="text-slate-500 text-sm mb-4">© 2026 FactGuard Intelligence Systems. All rights reserved.</p>
          <p className="text-white font-bold tracking-widest text-xs uppercase">DESIGNED & ENGINEERED BY SURIYA SRI</p>
        </div>
      </footer>
    </div>
  );
}

export default App;
