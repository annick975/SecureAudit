import React, { useState } from 'react';

const App: React.FC = () => {
  const [code, setCode] = useState<string>(''); // State to hold the user input code
  const [vulnerabilities, setVulnerabilities] = useState<string>(''); // State to hold the output

  // Function to handle code input change
  const handleCodeChange = (event: React.ChangeEvent<HTMLTextAreaElement>) => {
    setCode(event.target.value);
  };

  // Function to check vulnerabilities
  const checkVulnerabilities = async () => {
    try {
      const response = await fetch('http://127.0.0.1:5000/analyze', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ code }),
      });
  
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }
  
      const result = await response.json();
      if (result.results && result.results.length > 0) {
        setVulnerabilities(result.results.join('\n')); // Access results directly
      } else {
        setVulnerabilities('No vulnerabilities found.');
      }
    } catch (error) {
      console.error('Error checking vulnerabilities:', error);
      setVulnerabilities('Error checking vulnerabilities.');
    }
  };
  
  

  return (
    <div className="min-h-screen flex flex-col items-center justify-center bg-[#020010] py-10">
      <h1 className="text-3xl font-bold text-yellow-900 mb-6">Python Code Vulnerability Checker</h1>
      
      <div className="w-full max-w-4xl p-6 bg-gray-200 rounded-lg shadow-md">
        <h3 className="text-lg font-semibold text-gray-900 mb-3">Paste your Python code:</h3>
        <textarea
          value={code}
          onChange={handleCodeChange}
          placeholder="Paste Python code here..."
          rows={10}
          className="w-full p-3 border border-gray-400 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 font-mono"
        />
      </div>

      <button
        onClick={checkVulnerabilities}
        className="mt-6 px-5 py-3 bg-yellow-900 text-white font-semibold rounded-lg shadow-md hover:bg-blue-600"
      >
        Check Vulnerabilities
      </button>

      <div className="w-full max-w-4xl p-6 bg-gray-200 rounded-lg shadow-md mt-6">
        <h3 className="text-lg font-semibold text-gray-900 mb-3">Vulnerabilities found:</h3>
        <textarea
          value={vulnerabilities}
          readOnly
          rows={10}
          className="w-full p-3 border border-gray-400 rounded-lg bg-gray-80 font-mono"
        />
      </div>
    </div>
  );
};

export default App;
