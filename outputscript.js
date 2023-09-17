// Retrieve the localStorage item
const storedData = localStorage.getItem('globalData');

// Check if the item exists in localStorage
if (storedData) {
  try {
    // Parse the JSON data into an object
    const guide0 = JSON.parse(storedData);
	const guide = guide0.travel_guide
	
	//console.log(guide.essential_travel_tips);

    // Modify the data as needed
	
		
	document.addEventListener('DOMContentLoaded', displayTravelGuide);

function displayTravelGuide() {
  displayItinerary();
  displayAccommodationRecommendations();
  displayTransportationTips();
  displayEssentialTravelTips();
}

function displayItinerary() {
  const itineraryDiv = document.getElementById('itinerary');

  for (const dayKey in guide.itinerary) {
    const dayDetails = guide.itinerary[dayKey];

    const card = document.createElement('div');
    card.classList.add('card');

    const title = document.createElement('h3');
    title.textContent = `Day ${dayKey.charAt(dayKey.length - 1)}: ${dayDetails.highlights[0]}`;

    const details = document.createElement('ul');
    dayDetails.details.forEach(detail => {
      const detailItem = document.createElement('li');
      detailItem.textContent = detail;
      details.appendChild(detailItem);
    });

    card.appendChild(title);
    card.appendChild(details);
    itineraryDiv.appendChild(card);
  }
}

function displayAccommodationRecommendations() {
  const accommodationDiv = document.getElementById('accommodation');

  const hotelOption = guide.accommodation_recommendations.hotel_option;
  const airbnbOption = guide.accommodation_recommendations.airbnb_option;

  const hotelCard = createCard('Hotel Option:', hotelOption);
  const airbnbCard = createCard('Airbnb Option:', airbnbOption);

  accommodationDiv.appendChild(hotelCard);
  accommodationDiv.appendChild(airbnbCard);
}

function displayTransportationTips() {
		  const transportationDiv = document.getElementById('transportation');

		  for (const key in guide.transportation_tips.tips) {
			const block = document.createElement('div');
			block.classList.add('card');

			const description = document.createElement('p');
			description.textContent = guide.transportation_tips.tips[key];

			block.appendChild(description);
			transportationDiv.appendChild(block);
		  }
		}


function displayEssentialTravelTips() {
		  const essentialDiv = document.getElementById('essential');

		  for (const key in guide.essential_travel_tips) {
			const block = document.createElement('div');
			block.classList.add('card');

			const title = document.createElement('h3');
			title.textContent = key;

			const description = document.createElement('p');
			description.textContent = guide.essential_travel_tips[key];

			block.appendChild(title);
			block.appendChild(description);
			essentialDiv.appendChild(block);
		  }
		}


function createCard(title, content) {
  const card = document.createElement('div');
  card.classList.add('card');

  const cardTitle = document.createElement('h3');
  cardTitle.textContent = title;

  const cardContent = document.createElement('p');
  cardContent.textContent = content;

  card.appendChild(cardTitle);
  card.appendChild(cardContent);

  return card;
}

	
	// Modification done


  } catch (error) {
    console.error('Error parsing JSON:', error);
  }
} else {
  console.error('No data found in localStorage');
}


