import React, { useState } from 'react';
import { Monitor, AlertTriangle, CheckCircle } from 'lucide-react';

function App() {
  // Mock data - later this will come from your FastAPI /api/dashboard
  const [pcs] = useState([
    { id: 'PC-01', user: 'James Alfaro', status: 'Active' },
    { id: 'PC-02', user: 'Krimsie Caparanga', status: 'Violation' },
    { id: 'PC-03', user: 'None', status: 'Offline' },
  ]);

  return (
    <div className="min-h-screen bg-gray-100 p-8">
      <h1 className="text-3xl font-bold mb-6 text-gray-800">CCS ComLab Monitoring</h1>
      
      <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
        {pcs.map((pc) => (
          <div key={pc.id} className="bg-white p-6 rounded-xl shadow-md border-l-4 
            ${pc.status === 'Violation' ? 'border-red-500' : 'border-green-500'}">
            <div className="flex justify-between items-center">
              <Monitor size={32} className="text-gray-600" />
              <span className={`px-3 py-1 rounded-full text-xs font-bold 
                ${pc.status === 'Violation' ? 'bg-red-100 text-red-600' : 'bg-green-100 text-green-600'}`}>
                {pc.status}
              </span>
            </div>
            <h2 className="text-xl font-semibold mt-4">{pc.id}</h2>
            <p className="text-gray-500">User: {pc.user}</p>
            
            {pc.status === 'Violation' && (
              <div className="mt-4 flex items-center text-red-500 text-sm">
                <AlertTriangle size={16} className="mr-1" />
                <span>Unauthorized App Detected!</span>
              </div>
            )}
          </div>
        ))}
      </div>
    </div>
  );
}

export default App;