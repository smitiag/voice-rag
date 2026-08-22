import React, { useState } from 'react';
import { askQuestion } from "./api";
import { 
  MessageSquare, 
  FileText, 
  Mic,  
  Send, 
  UploadCloud, 
  Trash2, 
  CheckCircle2, 
  Loader2,
  File,
  Sparkles,
  Search,
  RefreshCw,
  //MoreVertical,
  Activity
} from 'lucide-react';
type Tab = "chat" | "documents" | "voice";
interface SidebarProps {
  activeTab: Tab;
  setActiveTab: React.Dispatch<React.SetStateAction<Tab>>;
}

export default function App() {
  const [activeTab, setActiveTab] = useState<Tab>("chat");

  return (
    <div className="flex h-screen bg-slate-50 font-sans text-slate-900 overflow-hidden">
      {/* Sidebar Navigation */}
      <Sidebar activeTab={activeTab} setActiveTab={setActiveTab} />
      
      {/* Main Content Area */}
      <main className="flex-1 flex flex-col h-full overflow-hidden relative">
        {activeTab === 'chat' && <ChatView />}
        {activeTab === 'documents' && <DocumentsView />}
        {activeTab === 'voice' && <VoiceView />}
      </main>
    </div>
  );
}

function Sidebar({ activeTab, setActiveTab }: SidebarProps){
 const navItems: { id: Tab; label: string; icon: React.ElementType }[] = [
  { id: "chat", label: "Chat", icon: MessageSquare },
  { id: "documents", label: "Documents", icon: FileText },
  { id: "voice", label: "Voice", icon: Mic },
];

  return (
    <aside className="w-64 bg-white border-r border-slate-200 flex flex-col h-full z-10">
      <div className="p-6 flex items-center gap-3 border-b border-slate-100">
        <div className="w-8 h-8 rounded-lg bg-violet-600 flex items-center justify-center text-white">
          <Sparkles size={18} />
        </div>
        <h1 className="font-semibold text-lg tracking-tight">RAG Assistant</h1>
      </div>

      <nav className="flex-1 p-4 space-y-1">
        {navItems.map((item) => {
          const Icon = item.icon;
          const isActive = activeTab === item.id;
          return (
            <button
              key={item.id}
              onClick={() => setActiveTab(item.id)}
              className={`w-full flex items-center gap-3 px-4 py-3 rounded-xl transition-all duration-200 ${
                isActive 
                  ? 'bg-violet-50 text-violet-700 font-medium' 
                  : 'text-slate-600 hover:bg-slate-50 hover:text-slate-900'
              }`}
            >
              <Icon size={20} className={isActive ? 'text-violet-600' : 'text-slate-400'} />
              {item.label}
            </button>
          );
        })}
      </nav>
    </aside>
  );
}

function ChatView() {
  const [inputText, setInputText] = useState('');
  const [answer, setAnswer] = useState("");
  const [sources, setSources] = useState<string[]>([]);
  const [loading, setLoading] = useState(false);

  const suggestions = [
    "Summarize the latest Q3 report",
    "What is the remote work policy?",
    "Find guidelines for expense reporting"
  ];


  const sendMessage = async () => {
    {answer && (
  <div className="flex flex-col items-start w-full">
    <div className="bg-white border border-slate-200 px-6 py-5 rounded-2xl rounded-tl-sm max-w-[85%] shadow-sm">
      <p className="text-slate-700 leading-relaxed">{answer}</p>

      <div className="mt-4">
        <p className="text-xs font-medium text-slate-500 mb-2">Sources</p>

        <div className="flex flex-wrap gap-2">
          {sources.map((_, i) => (
            <div
              key={i}
              className="bg-slate-100 px-3 py-1 rounded-lg text-sm"
            >
              Source {i + 1}
            </div>
          ))}
        </div>
      </div>
    </div>
  </div>
)}
  if (!inputText.trim()) return;

  setLoading(true);

  try {
    const data = await askQuestion(inputText);

    setAnswer(data.answer);
    setSources(data.retrieved_chunks);
    setInputText("");
  } catch (err) {
    setAnswer("Backend connection failed");
    setSources([]);
  } finally {
    setLoading(false);
  }
};

  return (
    <div className="flex-1 flex flex-col h-full bg-white max-w-5xl mx-auto w-full border-x border-slate-100 shadow-sm">
      {/* Chat Header */}
      <header className="px-8 py-6 border-b border-slate-100 bg-white z-10">
        <h2 className="text-2xl font-semibold text-slate-800">Chat</h2>
        <p className="text-slate-500 text-sm mt-1">Ask questions from your knowledge base</p>
      </header>

      {/* Chat History Area */}
      <div className="flex-1 overflow-y-auto p-8 space-y-8 bg-slate-50/50">
        
        {/* User Message */}
        <div className="flex flex-col items-end w-full">
          <div className="bg-violet-600 text-white px-6 py-4 rounded-2xl rounded-tr-sm max-w-[80%] shadow-sm">
            <p>What is our company policy on taking extended leave?</p>
          </div>
        </div>

        {/* AI Response */}
        <div className="flex flex-col items-start w-full">
          <div className="bg-white border border-slate-200 px-6 py-5 rounded-2xl rounded-tl-sm max-w-[85%] shadow-sm">
            <p className="text-slate-700 leading-relaxed">
               {loading ? "Generating answer..." : answer}
            </p>
            
            {/* Sources Section */}
            <div className="mt-5 pt-4 border-t border-slate-100">
              <div className="flex items-center gap-2 mb-3">
                <Search size={14} className="text-slate-400" />
                <span className="text-xs font-medium text-slate-500 uppercase tracking-wider">Sources Retrieved</span>
              </div>
              <div className="flex flex-wrap gap-2">
               {sources.map((_, index) => (
             <div
               key={index}
               className="flex items-center gap-2 bg-slate-50 border border-slate-200 px-3 py-1.5 rounded-lg text-sm"
               >
      <File size={14} className="text-violet-500" />
      <span className="text-slate-700 font-medium">
        Source {index + 1}
      </span>
    </div>
  ))}
</div>
            </div>
          </div>
        </div>

      </div>

      {/* Input Area */}
      <div className="p-6 bg-white border-t border-slate-100">
        {/* Suggested Questions */}
        <div className="flex gap-2 mb-4 overflow-x-auto pb-2 scrollbar-hide">
          {suggestions.map((suggestion, idx) => (
            <button 
              key={idx}
              onClick={() => setInputText(suggestion)}
              className="whitespace-nowrap px-4 py-2 bg-slate-50 hover:bg-violet-50 hover:text-violet-700 border border-slate-200 hover:border-violet-200 rounded-full text-sm text-slate-600 transition-colors"
            >
              {suggestion}
            </button>
          ))}
        </div>

        {/* Input Box */}
        <div className="relative flex items-center">
          <input
            type="text"
            value={inputText}
            onChange={(e) => setInputText(e.target.value)}
            placeholder="Ask anything..."
            className="w-full pl-6 pr-24 py-4 bg-slate-50 border border-slate-200 rounded-2xl focus:outline-none focus:ring-2 focus:ring-violet-500/20 focus:border-violet-500 transition-all text-slate-700 placeholder:text-slate-400"
          />
          <div className="absolute right-2 flex items-center gap-1">
            <button className="p-2 text-slate-400 hover:text-violet-600 hover:bg-violet-50 rounded-xl transition-colors">
              <Mic size={20} />
            </button>
            <button
  onClick={sendMessage}
  disabled={loading}
  className={`p-2 rounded-xl transition-colors ${
    inputText.trim()
      ? "bg-violet-600 text-white shadow-sm hover:bg-violet-700"
      : "bg-slate-100 text-slate-400"
  }`}
>
              <Send size={18} />
            </button>
          </div>
        </div>
      </div>
    </div>
  );
}

function DocumentsView() {
  const documents = [
    { id: 1, name: 'Employee_Handbook_2024.pdf', status: 'Indexed', date: '2 hours ago' },
    { id: 2, name: 'Q3_Financial_Projections.xlsx', status: 'Indexed', date: 'Yesterday' },
    { id: 3, name: 'Engineering_Onboarding.md', status: 'Indexed', date: 'Yesterday' },
    { id: 4, name: 'Client_Meeting_Notes_Oct.docx', status: 'Processing', date: 'Just now' },
  ];

  return (
    <div className="flex-1 flex flex-col h-full bg-white max-w-5xl mx-auto w-full border-x border-slate-100 shadow-sm">
      <header className="px-8 py-6 border-b border-slate-100 flex justify-between items-center">
        <div>
          <h2 className="text-2xl font-semibold text-slate-800">Documents</h2>
          <p className="text-slate-500 text-sm mt-1">Manage files in your knowledge base</p>
        </div>
        <button className="flex items-center gap-2 bg-violet-600 hover:bg-violet-700 text-white px-4 py-2 rounded-lg font-medium transition-colors shadow-sm">
          <UploadCloud size={18} />
          Upload Files
        </button>
      </header>

      <div className="p-8 overflow-y-auto">
        {/* Simple Drag and Drop Area */}
        <div className="border-2 border-dashed border-slate-200 rounded-2xl p-10 flex flex-col items-center justify-center bg-slate-50 hover:bg-slate-100/50 hover:border-violet-300 transition-colors cursor-pointer mb-8">
          <div className="w-12 h-12 bg-white rounded-full flex items-center justify-center shadow-sm mb-4">
            <UploadCloud size={24} className="text-violet-500" />
          </div>
          <h3 className="text-slate-700 font-medium mb-1">Click to upload or drag and drop</h3>
          <p className="text-slate-500 text-sm">PDF, DOCX, TXT, or MD (max 10MB)</p>
        </div>

        {/* Document List */}
        <div>
          <h3 className="text-sm font-semibold text-slate-900 mb-4 uppercase tracking-wider">Uploaded Files</h3>
          <div className="bg-white border border-slate-200 rounded-xl overflow-hidden">
            {documents.map((doc, idx) => (
              <div 
                key={doc.id} 
                className={`flex items-center justify-between p-4 ${
                  idx !== documents.length - 1 ? 'border-b border-slate-100' : ''
                } hover:bg-slate-50 transition-colors group`}
              >
                <div className="flex items-center gap-4">
                  <div className={`p-2 rounded-lg ${
                    doc.name.endsWith('.pdf') ? 'bg-red-50 text-red-500' :
                    doc.name.endsWith('.xlsx') ? 'bg-green-50 text-green-500' :
                    doc.name.endsWith('.docx') ? 'bg-blue-50 text-blue-500' :
                    'bg-slate-100 text-slate-500'
                  }`}>
                    <File size={20} />
                  </div>
                  <div>
                    <p className="font-medium text-slate-800">{doc.name}</p>
                    <p className="text-xs text-slate-400 mt-0.5">Uploaded {doc.date}</p>
                  </div>
                </div>

                <div className="flex items-center gap-6">
                  {doc.status === 'Indexed' ? (
                    <div className="flex items-center gap-1.5 text-emerald-600 bg-emerald-50 px-2.5 py-1 rounded-md text-sm font-medium border border-emerald-100">
                      <CheckCircle2 size={14} />
                      Indexed
                    </div>
                  ) : (
                    <div className="flex items-center gap-1.5 text-amber-600 bg-amber-50 px-2.5 py-1 rounded-md text-sm font-medium border border-amber-100">
                      <Loader2 size={14} className="animate-spin" />
                      Processing
                    </div>
                  )}
                  <button className="text-slate-300 hover:text-red-500 transition-colors p-2 opacity-0 group-hover:opacity-100">
                    <Trash2 size={18} />
                  </button>
                </div>
              </div>
            ))}
          </div>
        </div>
      </div>
    </div>
  );
}

function VoiceView() {
  // States: 'idle' | 'listening' | 'processing' | 'answered'
  const [voiceState, setVoiceState] = useState('idle');
  const [transcript, setTranscript] = useState('');

  // Simulate a realistic voice interaction flow
  const handleMicClick = () => {
    if (voiceState === 'idle' || voiceState === 'answered') {
      setVoiceState('listening');
      setTranscript('');
      
      // Simulate listening for 3 seconds
      setTimeout(() => {
        setVoiceState('processing');
        setTranscript("How many vacation days do I get in my first year?");
        
        // Simulate processing RAG answer for 2 seconds
        setTimeout(() => {
          setVoiceState('answered');
        }, 2500);
      }, 3000);
    } else {
      // Allow user to cancel mid-way
      setVoiceState('idle');
      setTranscript('');
    }
  };

  return (
    <div className="flex-1 flex flex-col h-full bg-slate-50 max-w-5xl mx-auto w-full relative">
      
      <div className="flex-1 flex flex-col items-center justify-center p-8">
        
        {/* Top Status Text */}
        <div className="h-12 flex items-center justify-center mb-8">
          {voiceState === 'idle' && (
            <p className="text-slate-500 font-medium animate-pulse">Tap the microphone to speak</p>
          )}
          {voiceState === 'listening' && (
            <div className="flex items-center gap-2 text-violet-600 font-medium">
              <Activity size={20} className="animate-pulse" />
              Listening...
            </div>
          )}
          {voiceState === 'processing' && (
            <div className="flex items-center gap-2 text-slate-600 font-medium">
              <RefreshCw size={20} className="animate-spin text-violet-600" />
              Generating answer...
            </div>
          )}
        </div>

        {/* Central Microphone Button */}
        <div className="relative mb-12">
          {voiceState === 'listening' && (
            <>
              <div className="absolute inset-0 bg-violet-400 rounded-full animate-ping opacity-20 scale-150"></div>
              <div className="absolute inset-0 bg-violet-400 rounded-full animate-pulse opacity-40 scale-125"></div>
            </>
          )}
          <button 
            onClick={handleMicClick}
            className={`relative z-10 w-32 h-32 rounded-full flex items-center justify-center transition-all duration-300 shadow-xl ${
              voiceState === 'listening' 
                ? 'bg-violet-600 text-white scale-110 shadow-violet-500/30' 
                : 'bg-white text-slate-700 hover:bg-slate-50 border border-slate-200'
            }`}
          >
            <Mic size={48} className={voiceState === 'listening' ? 'animate-pulse' : ''} />
          </button>
        </div>

        {/* Display Transcript and Answer */}
        <div className={`w-full max-w-2xl transition-all duration-500 flex flex-col items-center ${
          (voiceState === 'processing' || voiceState === 'answered') 
            ? 'opacity-100 translate-y-0' 
            : 'opacity-0 translate-y-8 pointer-events-none'
        }`}>
          
          <div className="bg-white px-6 py-4 rounded-2xl shadow-sm border border-slate-100 text-center mb-6 inline-block">
            <p className="text-sm text-slate-400 uppercase tracking-wider font-semibold mb-1">You said</p>
            <p className="text-lg text-slate-800 font-medium">"{transcript}"</p>
          </div>

          {voiceState === 'answered' && (
            <div className="bg-white w-full rounded-2xl shadow-lg border border-slate-200 overflow-hidden transform transition-all duration-500 animate-in fade-in slide-in-from-bottom-4">
              <div className="p-6">
                <div className="flex items-center gap-2 text-violet-600 mb-3">
                  <Sparkles size={18} />
                  <span className="font-semibold text-sm tracking-wide uppercase">RAG Answer</span>
                </div>
                <p className="text-slate-700 text-lg leading-relaxed">
                  During your first year of employment, you accrue <strong className="text-slate-900">15 vacation days</strong> (PTO). This increases to 20 days starting your second year. Note that sick leave is tracked separately.
                </p>
              </div>
              <div className="bg-slate-50 border-t border-slate-100 p-4 px-6">
                <p className="text-xs text-slate-500 uppercase font-semibold tracking-wider mb-2">Sources</p>
                <div className="flex gap-2">
                  <div className="flex items-center gap-1.5 bg-white border border-slate-200 px-2.5 py-1 rounded-md text-xs font-medium text-slate-600 shadow-sm">
                    <File size={12} className="text-violet-500" />
                    Employee_Handbook_2024.pdf
                  </div>
                  <div className="flex items-center gap-1.5 bg-white border border-slate-200 px-2.5 py-1 rounded-md text-xs font-medium text-slate-600 shadow-sm">
                    <File size={12} className="text-violet-500" />
                    Benefits_Overview.md
                  </div>
                </div>
              </div>
            </div>
          )}

        </div>
      </div>
    </div>
  );
}