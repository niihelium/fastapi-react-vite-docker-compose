import React from 'react';
import { useNavigate } from 'react-router-dom';

function Home() {
    const navigate = useNavigate();

    const handleClick = () => {
        navigate('/greet')
    };

    return (
        <div className="center">
            <h1>React app</h1>
            <button onClick={handleClick}>Greet</button>
        </div>
    );
}

export default Home;
