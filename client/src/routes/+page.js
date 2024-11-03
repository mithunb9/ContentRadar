export const load = ({ params }) => {
	return {
		recommendations: [
			{ link: 'https://www.streameast.gd/game/cfb/82148814', confidence: 0.89 },
			{ link: 'https://svelte.dev/docs/kit/load', confidence: 0.2 },
			{
				link: 'https://stackoverflow.com/questions/34600003/converting-json-to-string-in-python',
				confidence: 0.9
			}
		]
	};
};
