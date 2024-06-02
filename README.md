# Patient Report Analysis Project

## Description

This project aims to analyze patient medical reports in PDF format to extract relevant information, provide insights into the patient's health condition, and offer recommendations for potential diseases and health risks. The system leverages multiple AI agents to process and analyze the data, giving structured feedback in an easily understandable format.

## Approach

The project uses a multi-agent system to handle different tasks:
1. **Report Reading**: Extract data from the patient's medical report in PDF format.
2. **Health Analysis**: Analyze the extracted data to summarize the patient's health condition and potential diseases.
3. **Recommendations**: Provide health recommendations, treatment suggestions, and relevant articles for further reading.

These tasks are performed sequentially, with each agent specializing in a specific role.

## Code Description

### Agents

1. **Report Reader**
   - **Role**: Reads the PDF report and extracts data.
   - **Goal**: Provide the extracted data in a structured JSON format.
   - **Tools**: Uses `extract_data_from_pdf` and `SerperDevTool` for PDF data extraction and additional tools.
   - **LLM**: Utilizes `ChatOpenAI` with the `gpt-3.5-turbo` model.

2. **Doctor**
   - **Role**: Analyzes the extracted data to provide a summary of the patient's health condition.
   - **Goal**: Identify possible diseases and health risks, explaining them in simple language.
   - **Tools**: Uses `SerperDevTool` for additional data.
   - **LLM**: Utilizes `ChatOpenAI` with the `gpt-3.5-turbo` model.

3. **Recommendation Writer**
   - **Role**: Provides health recommendations and treatment suggestions based on the analysis.
   - **Goal**: Suggest ways to cure abnormalities, offer home remedies, and provide article links for more information.
   - **Tools**: Uses `SerperDevTool` for additional resources.
   - **LLM**: Utilizes `ChatOpenAI` with the `gpt-3.5-turbo` model.

### Tasks

1. **Task 1**: Extract data from the patient report and format it as JSON.
2. **Task 2**: Analyze the extracted data and provide detailed insights into the patient's health.
3. **Task 6**: Write recommendations based on the health analysis, including treatment methods and relevant articles.

### Resources Used

- **OpenAI GPT-3.5**: For language processing and generating insights and recommendations.
- **Camelot**: For extracting tables from PDF files.
- **CrewAI**: For managing and orchestrating the agents and tasks.
- **SerperDevTool**: For additional data extraction and processing.

## Future Enhancements

- **Enhanced Data Extraction**: Improve the accuracy of data extraction from PDFs, especially for complex reports.
- **Integration with More LLMs**: Incorporate other language models like Ollama to compare and enhance the analysis.
- **Real-Time Updates**: Allow real-time updates and monitoring of patient health data.
- **Broader Recommendations**: Include more comprehensive health recommendations and support for a wider range of medical conditions.
- **User Interface**: Develop a user-friendly interface for easier interaction with the system.
- **Emergency Report Marking**: Implement functionality to categorize reports by urgency using a color-coded system (red/orange/yellow) based on the severity of the results.

## Method to Run the Script

1. **Install Required Libraries**:
   Ensure you have all the necessary libraries installed. You can install the required packages using pip:

   ```sh
   pip install -r requirements.txt
   ```

2. **Set Environment Variables**:
   Set your OpenAI and Serper API keys in .env file:

   ```sh
   export OPENAI_API_KEY="your_openai_api_key"
   export SERPER_API_KEY="your_serper_api_key"
   ```

3. **Prepare the PDF File**:
   Place the patient's PDF report in the same directory as the script or provide the path to the PDF file.

4. **Run the Script**:
   Execute the `index.py` script:

   ```sh
   python index.py
   ```

   The script will process the PDF report, analyze the data, and provide insights and recommendations.

## References

- OpenAI: https://openai.com/
- CrewAI: https://crew.ai/
- SerperDevTool: https://serper.dev/
- Matthew Berman: https://www.youtube.com/@matthew_berman