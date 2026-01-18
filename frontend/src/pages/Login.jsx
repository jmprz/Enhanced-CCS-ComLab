import { useState } from 'react';

const Login = () => {
  const [formData, setFormData] = useState({ student_id: '', password: '' });

 const handleLogin = async (e) => {
  e.preventDefault();
  try {
    const response = await fetch("http://localhost:8000/login", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(formData),
    });

    const data = await response.json();

    if (response.ok) {
      alert("Login Successful!");
    } else {
      // If it's a validation error, data.detail is an array
      const errorMsg = typeof data.detail === 'string' 
        ? data.detail 
        : JSON.stringify(data.detail); 
      
      alert("Login Failed: " + errorMsg);
      console.log("Full Error details:", data.detail);
    }
  } catch (error) {
    alert("Connection Error. Is the backend running?");
  }
};

  return (
    <div style={{ display: 'flex', justifyContent: 'center', marginTop: '50px' }}>
      <form onSubmit={handleLogin} style={{ border: '1px solid #ccc', padding: '20px', borderRadius: '8px' }}>
        <h2>CCS ComLab Login</h2>
        <div style={{ marginBottom: '10px' }}>
          <label>Student/Faculty ID:</label><br/>
          <input 
            type="text" 
            onChange={(e) => setFormData({...formData, student_id: e.target.value})}
            required 
          />
        </div>
        <div style={{ marginBottom: '10px' }}>
          <label>Password:</label><br/>
          <input 
            type="password" 
            onChange={(e) => setFormData({...formData, password: e.target.value})}
            required 
          />
        </div>
        <button type="submit" style={{ width: '100%', padding: '10px', background: '#007bff', color: 'white', border: 'none' }}>
          Login
        </button>
      </form>
    </div>
  );
};

export default Login;