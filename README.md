# Memory-Powered AI Support Agent

## Overview

This project demonstrates an AI customer-support agent powered by persistent memory using Hindsight.

Traditional AI support agents may forget previous conversations and ask customers to repeat information. This project uses Hindsight to retain customer interactions, recall relevant history, and generate responses using that memory.

## Problem

A customer contacts support about an issue. If they contact support again later, a stateless AI agent may ask them to explain the problem again.

This creates a poor customer experience.

## Solution

Our agent uses three stages:

1. Retain - stores customer interactions in Hindsight.
2. Recall - retrieves relevant information from previous interactions.
3. Reflect - generates a response using the recalled context.

## Example

Customer: Priya Sharma

Issue:
- Windows 11
- App version 3.2
- Application crashes when uploading PDFs larger than 5MB
- Clearing cache did not solve the problem
- Ticket #1042

When Priya contacts support again, the agent recalls this information and responds without asking her to repeat everything.

## Technology

- Python
- Hindsight Cloud
- Hindsight Python Client
- AI agent workflow
- Persistent memory

## Architecture

Customer Interaction
        |
        v
   Hindsight Retain
        |
        v
 Persistent Memory
        |
        v
   Hindsight Recall
        |
        v
      Reflect
        |
        v
 Personalized Support Response

## Running the Project

Install the Hindsight client:

pip install hindsight-client

Add your Hindsight API key to agent.py and run:

python agent.py

## Important

Never commit your API key to GitHub.
