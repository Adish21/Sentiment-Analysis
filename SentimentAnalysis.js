import React, { useState } from 'react';
import './App.css';

export default function SentimentAnalysis() {
  const [link, setLink] = useState('');
  const [headline, setHeadline] = useState('');
  const [image, setImage] = useState(null);

  return (
    <div className='container'>
      <div className='content-box'>
        <h1 className='title'>SENTIMENT ANALYSIS</h1>
        <div className='input-group'>
          <label>COPY THE LINK OF THE ARTICLE</label>
          <input type='text' placeholder='Paste the Link Here' value={link} onChange={(e) => setLink(e.target.value)} />
        </div>
        <div className='separator'>or</div>
        <div className='input-group'>
          <label>COPY THE HEADLINE OF THE ARTICLE</label>
          <input type='text' placeholder='Paste the Headline Here' value={headline} onChange={(e) => setHeadline(e.target.value)} />
        </div>
        <div className='separator'>or</div>
        <div className='upload-section'>
          <label>UPLOAD THE IMAGE BELOW</label>
          <label className='upload-box'>
            <span>⬆️</span>
            <input type='file' className='hidden' onChange={(e) => setImage(e.target.files[0])} />
          </label>
        </div>
      </div>
    </div>
  );
}