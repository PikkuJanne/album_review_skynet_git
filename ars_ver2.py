import openai

API_KEY = "API-key"

class AlbumReviewGenerator:
    def __init__(self, api_key=API_KEY, model="text-davinci-003", max_tokens=250, temperature=0.7, completions=3, best_of=3, presence_penalty=0.5, frequency_penalty=0.5):
        self.__api_key = api_key  
        self._model = model  
        self._genre = "General"  # Protected attribute
        self.max_tokens = max_tokens
        self.temperature = temperature
        self.completions = completions
        self.best_of = best_of
        self.presence_penalty = presence_penalty
        self.frequency_penalty = frequency_penalty
        openai.api_key = self.__api_key

    def get_response(self, prompt):
        response = openai.Completion.create(
            model=self._model,
            prompt=prompt,
            max_tokens=self.max_tokens,
            temperature=self.temperature,
            n=self.completions,
            best_of=self.best_of,
            presence_penalty=self.presence_penalty,
            frequency_penalty=self.frequency_penalty
        )
        choices = [choice.text.strip() for choice in response.choices]
        return choices

    def generate_review(self, album_name, band, tracklist, release_date):
        pass

class RockAlbumReviewGenerator(AlbumReviewGenerator):
    def __init__(self, api_key=API_KEY, model="text-davinci-003", max_tokens=250, temperature=1.0, completions=1, best_of=1, presence_penalty=0.1, frequency_penalty=0.1):
        super().__init__(api_key, model, max_tokens, temperature, completions, best_of, presence_penalty, frequency_penalty)
        self._genre = "Rock"  # Using protected attribute
        self.__custom_prompt = "You are Lester Bangs, a renowned rock music journalist."  # Private attribute

    def generate_review(self, album_name, band, leadsongs):
        # Using private attribute in the prompt
        prompt = f"{self.__custom_prompt} Review the metal/rock album '{album_name}' by {band}, with the lead songs (emphasize these lead songs over the rest of the album):\n"
        for i, song in enumerate(leadsongs, start=1):
            prompt += f"{i}. {song}\n"
        prompt += "Review:"
        response = self.get_response(prompt)
        return response[0]

class PopAlbumReviewGenerator(AlbumReviewGenerator):
    def __init__(self, api_key=API_KEY, model="text-davinci-003", max_tokens=200, temperature=0.9, completions=1, best_of=1, presence_penalty=0.1, frequency_penalty=0.1):
        super().__init__(api_key, model, max_tokens, temperature, completions, best_of, presence_penalty, frequency_penalty)
        self._genre = "Pop"  # Using protected attribute

    def generate_review(self, album_name, band, leadsongs):
        prompt = f"You are Robert Christgau, a well-known music journalist. Review the pop album '{album_name}' by {band}, with the following lead songs (emphasize these lead songs over the rest of the album):\n"
        for i, song in enumerate(leadsongs, start=1):
            prompt += f"{i}. {song}\n"
        prompt += "Review:"
        response = self.get_response(prompt)
        return response[0]
