import React, { useState } from 'react';

export default function Dashboard({ onBack }) {
  const [activeTab, setActiveTab] = useState('scan');
  const [input, setInput] = useState('');
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState(null);
  const [chatLog, setChatLog] = useState([
    { role: 'ai', text: "Hello Suriya Sri. Please provide some news content, and I will analyze its linguistic integrity for you." }
  ]);
  const [chatInput, setChatInput] = useState('');

  const handleScan = async (mode = 'text') => {
    if (!input) return;
    setLoading(true);
    
    // Simulate Neural Network latency
    await new Promise(resolve => setTimeout(resolve, 1500));
    
    // JS Heuristic matching the original Python dummy model logic
    const t = input.toLowerCase();
    const isFake = t.includes('win') || t.includes('free') || t.includes('secret') || t.includes('shocking') || t.includes('money');
    
    const confidence = isFake ? 0.85 + (Math.random() * 0.14) : 0.70 + (Math.random() * 0.25);
    const polarity = isFake ? -0.4 + (Math.random() * 0.8) : 0.1 + (Math.random() * 0.8);
    const subjectivity = isFake ? 0.7 + (Math.random() * 0.3) : 0.2 + (Math.random() * 0.5);
    
    const data = {
      prediction: isFake ? 1 : 0,
      confidence,
      polarity,
      subjectivity
    };

    setResult(data);
    setChatLog(prev => [...prev, { role: 'ai', text: `I have analyzed the content. The authenticity score is ${(data.confidence * 100).toFixed(1)}%. Would you like me to generate a full report?` }]);
    setLoading(false);
  };

  const handleChat = (e) => {
    e.preventDefault();
    if (!chatInput) return;
    setChatLog(prev => [...prev, { role: 'user', text: chatInput }, { role: 'ai', text: "That's a great question! Based on my neural training, I recommend checking multiple sources for any claim that has a Bias Index over 60%." }]);
    setChatInput('');
  };

  const renderGauge = (value, label, color) => {
    const r = 40;
    const circ = 2 * Math.PI * r;
    const strokeDasharray = `${(value / 100) * circ} ${circ}`;
    return (
      <div className="flex flex-col items-center justify-center p-6 bg-black/20 rounded-2xl border border-white/5">
        <div className="relative w-32 h-32 flex items-center justify-center mb-4">
          <svg className="w-full h-full transform -rotate-90" viewBox="0 0 100 100">
            <circle cx="50" cy="50" r="40" fill="transparent" stroke="rgba(255,255,255,0.1)" strokeWidth="10" />
            <circle cx="50" cy="50" r="40" fill="transparent" stroke={color} strokeWidth="10" strokeDasharray={strokeDasharray} className="transition-all duration-1000" />
          </svg>
          <div className="absolute text-2xl font-black text-white">{value.toFixed(1)}</div>
        </div>
        <div className="text-slate-400 font-bold uppercase tracking-widest text-xs text-center">{label}</div>
      </div>
    );
  };

  return (
    <div className="min-h-screen bg-[#020617] text-white font-sans selection:bg-blue-500/30 overflow-auto">
      {/* Neural Background */}
      <div className="fixed inset-0 overflow-hidden pointer-events-none" style={{ background: 'radial-gradient(circle at 50% 50%, #1e1b4b 0%, #020617 100%)' }}>
        <div className="absolute top-0 right-0 w-96 h-96 bg-blue-600/20 blur-[120px] rounded-full"></div>
        <div className="absolute bottom-0 left-0 w-96 h-96 bg-pink-600/10 blur-[120px] rounded-full"></div>
      </div>

      <div className="relative max-w-6xl mx-auto p-8 pt-20">
        <button onClick={onBack} className="absolute top-8 left-8 px-6 py-2 bg-slate-900/80 backdrop-blur-md border border-white/10 hover:bg-slate-800 rounded-full text-[10px] font-black tracking-widest transition-all shadow-xl flex items-center gap-2 text-white z-50">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="3" strokeLinecap="round" strokeLinejoin="round"><path d="M19 12H5M12 19l-7-7 7-7"/></svg>
          BACK TO LANDING
        </button>

        {/* Header */}
        <div className="mb-12 mt-12">
          <h1 className="text-6xl md:text-8xl font-black tracking-tighter mb-2" style={{ background: 'linear-gradient(90deg, #38bdf8, #818cf8, #ec4899)', WebkitBackgroundClip: 'text', WebkitTextFillColor: 'transparent' }}>
            FACTGUARD AI
          </h1>
          <p className="text-xl text-slate-400">Autonomous Misinformation Neural Network | Suriya Sri</p>
        </div>

        {/* Tabs */}
        <div className="flex gap-8 border-b border-white/10 mb-8 overflow-x-auto">
          {[
            { id: 'scan', label: '🧠 NEURAL SCAN' },
            { id: 'web', label: '🌐 WEB SCRAPER' },
            { id: 'chat', label: '💬 AI ASSISTANT' }
          ].map(tab => (
            <button key={tab.id} onClick={() => setActiveTab(tab.id)} className={`pb-4 text-sm font-black tracking-widest transition-colors whitespace-nowrap ${activeTab === tab.id ? 'text-blue-400 border-b-2 border-blue-400' : 'text-slate-500 hover:text-slate-300'}`}>
              {tab.label}
            </button>
          ))}
        </div>

        {/* Content Panel */}
        <div className="bg-slate-900/50 backdrop-blur-2xl border border-blue-500/20 rounded-[32px] p-8 shadow-[0_0_40px_rgba(0,0,0,0.5)]">
          {activeTab === 'scan' && (
            <div className="animate-in fade-in slide-in-from-bottom-4 duration-500">
              <textarea value={input} onChange={(e) => setInput(e.target.value)} placeholder="Paste data here for neural analysis..." className="w-full h-48 bg-black/40 border border-white/10 rounded-2xl p-6 text-lg text-white placeholder-slate-600 focus:outline-none focus:border-blue-500/50 mb-6" />
              <button onClick={() => handleScan('text')} disabled={loading} className="px-8 py-4 bg-blue-600 hover:bg-blue-500 rounded-xl font-black tracking-widest transition-all shadow-lg shadow-blue-500/20 disabled:opacity-50 flex items-center gap-2">
                {loading ? 'ANALYZING NEURAL PATTERNS...' : 'EXECUTE SCAN'}
              </button>
            </div>
          )}

          {activeTab === 'web' && (
            <div className="animate-in fade-in slide-in-from-bottom-4 duration-500">
              <input type="text" value={input} onChange={(e) => setInput(e.target.value)} placeholder="Enter Target URL (e.g. https://news.com/article)" className="w-full bg-black/40 border border-white/10 rounded-2xl p-6 text-lg text-white placeholder-slate-600 focus:outline-none focus:border-blue-500/50 mb-6" />
              <button onClick={() => handleScan('url')} disabled={loading} className="px-8 py-4 bg-purple-600 hover:bg-purple-500 rounded-xl font-black tracking-widest transition-all shadow-lg shadow-purple-500/20 disabled:opacity-50">
                {loading ? 'CONNECTING TO GLOBAL WEB...' : 'SCRAPE & SCAN'}
              </button>
            </div>
          )}

          {activeTab === 'chat' && (
            <div className="animate-in fade-in slide-in-from-bottom-4 duration-500 flex flex-col h-96">
              <div className="flex-1 overflow-y-auto mb-6 pr-4">
                {chatLog.map((msg, i) => (
                  <div key={i} className={`mb-4 max-w-[80%] ${msg.role === 'ai' ? 'mr-auto bg-blue-500/10 border-l-4 border-blue-500' : 'ml-auto bg-white/5 border-r-4 border-white'} p-4 rounded-xl`}>
                    <div className="text-xs font-black tracking-widest opacity-50 mb-2 uppercase">{msg.role === 'ai' ? 'Neural AI' : 'User'}</div>
                    <div className="text-lg italic">{msg.text}</div>
                  </div>
                ))}
              </div>
              <form onSubmit={handleChat} className="flex gap-4">
                <input type="text" value={chatInput} onChange={e => setChatInput(e.target.value)} placeholder="Ask AI Assistant..." className="flex-1 bg-black/40 border border-white/10 rounded-xl px-6 py-4 focus:outline-none focus:border-blue-500/50" />
                <button type="submit" className="px-8 py-4 bg-blue-600 rounded-xl font-black">SEND</button>
              </form>
            </div>
          )}
        </div>

        {/* Results Dashboard */}
        {result && (
          <div className="mt-12 animate-in slide-in-from-bottom-8 duration-1000">
            <div className="bg-slate-900/50 backdrop-blur-2xl border border-white/10 rounded-[32px] p-10 shadow-2xl">
              <h2 className={`text-4xl md:text-5xl font-black tracking-tighter mb-12 ${result.prediction === 0 ? 'text-emerald-500' : 'text-rose-500'}`}>
                {result.prediction === 0 ? '✅ NEURAL VERIFIED: AUTHENTIC' : '🚩 NEURAL ALERT: MISINFORMATION'}
              </h2>
              <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
                {renderGauge(result.confidence * 100, "Neural Confidence", result.prediction === 0 ? "#10b981" : "#f43f5e")}
                {renderGauge((result.polarity + 1) * 50, "Linguistic Tone", "#8b5cf6")}
                {renderGauge(result.subjectivity * 100, "Bias Index", "#f59e0b")}
              </div>
            </div>
          </div>
        )}

        <div className="text-center mt-32 mb-12 opacity-30 text-xs font-black tracking-[0.4em] uppercase">
          FACTGUARD NEURAL | AUTONOMOUS VERSION | SURIYA SRI
        </div>
      </div>
    </div>
  );
}
