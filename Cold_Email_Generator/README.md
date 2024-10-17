# AI-Powered Cold Email Generator

## Overview

This project automates the creation of personalized cold emails tailored to specific job postings. It is designed for **Business Development Executives (BDEs)** in companies like Infosys, TCS, and other IT firms, helping them reach potential clients efficiently. By leveraging AI language models, the tool generates relevant, job-specific emails, reducing the time and effort required to manually craft each message.

## Problem Statement

Companies offering software services often need to reach out to potential clients via cold emails. Manually writing these emails can be time-consuming, especially when aligning them with job postings and required skills. This project automates that process, allowing BDEs to generate customized emails quickly and accurately.

## Features

- **Job-Specific Email Generation**: AI-based email generation based on job listings.
- **Tailored Messaging**: Emails are customized to match the required skills in the job posting.
- **Automated Workflow**: Reduces manual effort, streamlining business outreach efforts.
- **Easy-to-Use Interface**: Built with **Streamlit** for simple and intuitive user interaction.

## Technologies Used

- **AI Language Models**: Generates coherent and tailored emails.
- **LangChain**: Simplifies LLM (Large Language Model) application development.
- **Chroma Vector Database**: For efficient storage and retrieval of vectorized data.
- **GroqCloud**: Provides fast inference for running large language models.
- **Llama 3.1**: An AI model by Meta for generating high-quality language outputs.
- **Streamlit**: Framework for building and deploying the app.

## Installation & Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/sachinmotwani20/Deep-Learning/tree/24f579bf0503c65935fe3cb059d519988c1592e4/Cold_Email_Generator
   ```

2. Navigate to the project directory:
   ```bash
   cd Cold_Email_Generator/App
   ```
   
3. Run the Streamlit app:
   ```bash
   streamlit run main.py
   ```


## Files in the Repository

- **main.py**: The entry point for the Streamlit app.
- **chains.py**: Contains logic for AI model interactions using LangChain.
- **portfolio.py**: Includes the job analysis and email generation functionality.
- **utils.py**: Utility functions for processing and integration.
- **vectorstore/**: Stores vectorized data using Chroma.
- **Note.txt**: Additional project notes.

## Key Resources

- **GroqCloud** - Fast API for running LLM models.
- **Meta Llama 3.1** - AI language model used for generating emails.
- **LangChain** - Framework for building LLM applications.
- **Chroma** - Open-source vector database.
- **Streamlit** - Application framework for building the user interface.
