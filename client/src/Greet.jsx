import React, { useEffect, useState } from 'react';

const API_URL = import.meta.env.VITE_API_URL;

function Greet() {
    const [data, setData] = useState(null);
    const [error, setError] = useState(null);

    const fetchData = async () => {
        try {
            const response = await fetch(API_URL + '/greet');
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            const jsonData = await response.json();
            setData(jsonData);
        } catch (error) {
            setError(error);
        }
    };

    useEffect(() => {
        fetchData();
    }, []);

    return (
        <div className="center">
            {error && <p>Error: {error.message}</p>}
            {data && (
                <div>
                    <p>Data received:</p>
                    <p>Hello, {data['username']}!</p>
                </div>
            )}
        </div>
    );
}

export default Greet;