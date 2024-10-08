"use client";

import React, { useState } from 'react';

const Page = () => {
  const [key, setKey] = useState('');
  const [text, setText] = useState('');
  const [loading, setLoading] = useState(false); // Loader state

  const handleDownload = async (e) => {
      e.preventDefault();
      setLoading(true); // Start loading
      
      const data = new URLSearchParams();
      data.append('key', key);
      data.append('text', text);

      try {
          const response = await fetch('http://127.0.0.1:8000/ip-checker/', {
              method: 'POST',
              headers: {
                  'Content-Type': 'application/x-www-form-urlencoded',
              },
              body: data.toString(),
          });

          if (!response.ok) {
              throw new Error('Network response was not ok');
          }
          
          const blob = await response.blob();
          
          const url = window.URL.createObjectURL(new Blob([blob]));
          
          const link = document.createElement('a');
          link.href = url;
          link.setAttribute('download', 'domain_status.csv');
          
          document.body.appendChild(link);
          link.click();
          
          link.parentNode.removeChild(link);
      } catch (error) {
          console.error('Error while downloading the CSV file:', error);
      } finally {
        setLoading(false); // End loading
    }
  };

  return (
    <>
    <span className="font-bold text-4xl">IP Checker</span>
    <div>
        <div className="border-dashed border border-zinc-500 w-full h-full rounded-lg">
        <form className='analyzer-form' onSubmit={handleDownload}>
            <label htmlFor="inputlabel">Input API</label>
            <input className='input-api'
                type="text"
                placeholder="Enter VirusTotal API key"
                value={key}
                onChange={(e) => setKey(e.target.value)}
                required
            />
            <label htmlFor="inputlabel">Input IP Addresses</label>
            <textarea className='input-ioc'
                placeholder="Enter IPs, one per line"
                value={text}
                onChange={(e) => setText(e.target.value)}
                required
            ></textarea>
            <div className='button-loader'>
            <button className='button-analyzer' type="submit">Analyze</button>
            {loading && <p>Please wait! Report will be downloaded once analyzed.....</p>} {/* Conditional loader */}</div>
        </form>
        </div>
    </div>
    </>
  )
}

export default Page