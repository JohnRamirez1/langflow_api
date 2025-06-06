# LangFlow API Agents

This repository contains Python scripts that interact with LangFlow API endpoints to perform:

- **Travel Planning**: Generate personalized travel itineraries.
- **Diet Analysis**: Analyze food items for dietary evaluation.
- **Price Dealer**: Searches and compares prices of a product on the web.
- **Social Media**: Extract and analyze social media data.

Each script sends an HTTP request to a LangFlow API endpoint and processes the response.

---

## Files

- **API_travel_planning_agent.py**  
  Generates a travel itinerary based on input preferences like origin, destination, date, and traveler interests.

- **API_diet_analysis_agent.py**  
  Evaluates a list of food items for dietary assessment.

- **API_price_dealer_agent.py**  
This flow searches and compares prices of a product on the web.

- **API_social_media_agent.py**  
  Extract social media data with **Apify Actors** and analyze the data with an **Agent**..
---

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/<your-username>/<your-repository>.git
cd <your-repository>
```

### 2. (Optional) Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

If you don't have a `requirements.txt`, install manually:

```bash
pip install requests python-dotenv
```

### 4. Set up environment variables

Create a `.env` file in the root of your project:

```env
LF_TRAVEL_AGENT=<YOUR_APPLICATION_TOKEN_FOR_TRAVEL>
LF_DIET_EVALUATION=<YOUR_APPLICATION_TOKEN_FOR_DIET>
LF_SOCIALMEDIA=<YOUR_APPLICATION_TOKEN_FOR_SOCIALMEDIA>
LF_PRICEDEALER=<YOUR_APPLICATION_TOKEN_FOR_PRICEDEALER>
```

Replace the placeholders with your actual API tokens.

---

## How to Use

### Travel Planning Agent

Run the Travel Planning Agent script:

```bash
python API_travel_planning_agent.py
```

Example input sent to API:

> "Create a travel itinerary for a trip from São Paulo to Uberlândia, MG on August 23, 2024. The traveler enjoys drinking beer, eating pão de queijo, and drinking special coffee."

The generated itinerary will be printed in the terminal.

---

### Diet Analysis Agent

Run the Diet Analysis Agent script:

```bash
python API_diet_analysis_agent.py
```

Example input sent to API:

> "eggs, chocolate, bread, and meat"

The diet evaluation result will be printed in the terminal.

---

## Project Structure

```plaintext
├── API_travel_planning_agent.py
├── API_diet_analysis_agent.py
├── .env               # Environment variables (should not be committed)
├── requirements.txt   # Project dependencies
├── README.md          # Project documentation
```

---

## Error Handling

Both scripts handle:

- HTTP request failures
- API response parsing errors

Clear error messages are printed if an exception occurs.

---

## Requirements

- Python 3.8+
- `requests`
- `python-dotenv`

Example `requirements.txt`:

```txt
requests
python-dotenv
```

---

## Example `.env` file

```env
LF_TRAVEL_AGENT=your_travel_agent_token_here
LF_DIET_EVALUATION=your_diet_evaluation_token_here
```

---

## License

This project is licensed under the [MIT License](LICENSE).

---

## Author

Developed by [John Ramirez](https://github.com/JohnRamirez1).

Feel free to open issues or submit pull requests to improve the project!
