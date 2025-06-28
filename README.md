# Task 1: Machine Learning – Multi-Objective Optimization

## Problem Statement

This task involves defining and solving a multi-objective optimization problem using a dataset of choice. The objective is to identify optimal trade-offs between at least three conflicting numerical goal variables. For this task, the Auto MPG dataset was used, which includes various performance-related metrics of cars.

## Dataset Selection

- **Dataset:** Auto MPG (from kaggle - https://www.kaggle.com/datasets/uciml/autompg-dataset)
- **Selected Features:**
  - `mpg` (Miles Per Gallon) – to be maximized
  - `horsepower` – to be maximized
  - `weight` – to be minimized

These variables represent conflicting goals. For example, higher horsepower can lead to lower mpg, and reducing weight can affect engine performance.

## Problem Formulation

**Objective:**  
Find the optimal balance between fuel efficiency, engine power, and vehicle weight.

**Constraints:**  
- All features are normalized to a range of [0, 1]
- The optimization problem is subject to bounds within this normalized space

## Optimization Strategy

A **Weighted Sum Method** was used to reduce the multi-objective problem to a single scalar objective: Objective = -0.4 * mpg - 0.4 * horsepower + 0.2 * weight

