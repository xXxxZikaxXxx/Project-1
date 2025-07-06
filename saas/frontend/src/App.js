import React from 'react';
import { GoogleLogin } from '@react-oauth/google';
import axios from 'axios';

function App() {
  const handleSuccess = async (credentialResponse) => {
    try {
      const res = await axios.post(`${process.env.REACT_APP_API_URL}/auth/google/`, {
        access_token: credentialResponse.credential,
      });
      localStorage.setItem('token', res.data.access_token);
    } catch (err) {
      console.error(err);
    }
  };

  return (
    <div>
      <h1>Welcome</h1>
      <GoogleLogin onSuccess={handleSuccess} />
    </div>
  );
}

export default App;
