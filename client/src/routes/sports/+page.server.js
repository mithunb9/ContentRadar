// src/routes/your-route/+page.server.js
export const load = async ({ fetch }) => {
	let recommendations = [
		{ link: 'https://www.streameast.gd/game/cfb/82148814', confidence: 0.4 },
		{
			link: 'https://cloudcannon.com/tutorials/sveltekit-beginner-tutorial/sveltekit-components/',
			confidence: 0.5
		},
		{
			link: 'https://stackoverflow.com/questions/34600003/converting-json-to-string-in-python',
			confidence: 0.1
		},
		{
			link: 'https://stackoverflow.com/questions/34600003/converting-json-to-string-in-python',
			confidence: 0.8
		},
		{
			link: 'https://stackoverflow.com/questions/34600003/converting-json-to-string-in-python',
			confidence: 0.7
		}
	];

	let embed = [];

	for (let recommendation of recommendations) {
		try {
			// Fetch the embed data from your backend server
			const response = await fetch(`http://127.0.0.1:5000/embed?link=${recommendation.link}`);
			if (response.ok) {
				const embed_data = await response.json();
				embed.push({ ...recommendation, ...embed_data });
			} else {
				console.error(
					`Failed to fetch data from ${recommendation.link}, status: ${response.status}`
				);
			}
		} catch (error) {
			console.error(`Error fetching data from ${recommendation.link}:`, error);
		}
	}

	// Return the fetched data
	return {
		data: embed
	};
};
