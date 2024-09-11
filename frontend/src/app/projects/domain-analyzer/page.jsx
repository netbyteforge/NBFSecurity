"use client";

import React, { useState } from 'react';

const Page = () => {
  const [key, setKey] = useState('');
  const [text, setText] = useState('');

  const handleDownload = async (e) => {
      e.preventDefault();
      
      const data = new URLSearchParams();
      data.append('key', key);
      data.append('text', text);

      try {
          const response = await fetch('http://127.0.0.1:8000/domain-checker/', {
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
      }
  };

  return (
    <div>
        <form onSubmit={handleDownload}>
            <input
                type="text"
                placeholder="Enter key"
                value={key}
                onChange={(e) => setKey(e.target.value)}
                required
            />
            <textarea
                placeholder="Enter domains, one per line"
                value={text}
                onChange={(e) => setText(e.target.value)}
                required
            ></textarea>
            <button type="submit">Download CSV</button>
        </form>
    </div>
  )
}

export default Page