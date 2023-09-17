let globalData;

document.getElementById('travelForm').addEventListener('submit', function(event) {
  event.preventDefault(); // Prevents the default form submission behavior

  const formData = {
    destination: document.getElementById('destination').value,
    duration: document.getElementById('duration').value,
    interests: document.getElementById('interests').value,
    budget: document.getElementById('budget').value,
    accommodationPreferences: document.getElementById('accommodationPreferences').value,
    travelStyle: document.getElementById('travelStyle').value,
    specialRequirements: document.getElementById('specialRequirements').value
  };

  async function myFunction(formData) {
    const res = await fetch('http://127.0.0.1:5000/plan_trip', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(formData)
    });
    const data = await res.json();
    globalData = data;
    handleGlobalData(globalData); // Call a callback function with the globalData
  }

  myFunction(formData);
});

function handleGlobalData(data) {
  console.log('Received data:', data);
  // Store the data in localStorage
  localStorage.setItem('globalData', data);

}
