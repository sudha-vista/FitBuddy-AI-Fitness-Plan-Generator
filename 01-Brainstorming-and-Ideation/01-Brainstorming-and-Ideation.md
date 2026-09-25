# Phase 1 – Brainstorming & Ideation

**Project:** FitBuddy – AI Fitness Plan Generator

## 1. Project Title

FitBuddy – AI Fitness Plan Generator

## 2. Problem Statement

Users may find it difficult to create a structured fitness routine that matches a selected fitness goal and preferred workout intensity. FitBuddy addresses this by generating a structured seven-day workout plan, providing a general nutrition/recovery tip, and allowing the user to refine the plan through feedback.

## 3. Proposed Solution

FitBuddy is a web-based application that collects basic user information such as name, age, weight, fitness goal, and workout intensity. It uses a Google Gemini-powered AI layer to generate a seven-day workout plan and a nutrition/recovery tip. Users can submit feedback and receive a revised plan.

## 4. Objectives

• Generate a structured 7-day workout plan from user inputs.
• Provide a concise nutrition or recovery tip.
• Allow users to refine a plan through feedback.
• Store user and plan information using SQLite/SQLAlchemy.
• Provide an admin view of stored users and plans.
• Expose REST API endpoints and interactive API documentation.

## 5. Target Users

Primary users are individuals seeking general wellness-oriented workout planning. The project also provides an admin/coach/developer-oriented view for reviewing stored users and their plans.

## 6. Main Use Cases

Use Case 1: Create a personalized plan.
Use Case 2: View the generated plan and nutrition/recovery tip.
Use Case 3: Submit feedback and generate a revised plan.
Use Case 4: Review stored users and plans through the admin view.
Use Case 5: Access the REST API and Swagger documentation.

## 7. Expected Outcome

A working web application that accepts fitness inputs, generates a plan, stores the result, supports feedback-based revision, and presents the output through a browser interface.
