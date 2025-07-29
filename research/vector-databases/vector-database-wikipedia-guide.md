# Vector Database Guide - Wikipedia Summary

## Overview

A **vector database** (also known as vector store or vector search engine) is a specialized database that uses the vector space model to store vectors - fixed-length lists of numbers - along with other data items. These databases are designed to efficiently handle high-dimensional vector data and perform similarity searches.

## Key Concepts

### What are Vectors?
- **Mathematical representations** of data in high-dimensional space
- Each dimension corresponds to a **feature** of the data
- Number of dimensions can range from hundreds to tens of thousands
- A vector's position in space represents its characteristics
- Can represent words, phrases, documents, images, audio, and other data types

### Feature Vectors
Feature vectors are computed from raw data using:
- **Feature extraction algorithms**
- **Word embeddings**
- **Deep learning networks**

The goal is to ensure semantically similar data items receive feature vectors that are close to each other in the vector space.

## Core Techniques

Vector databases implement several key techniques for similarity search on high-dimensional vectors:

1. **Hierarchical Navigable Small World (HNSW) graphs** - Among the best performers in recent benchmarks
2. **Locality-sensitive Hashing (LSH) and Sketching**
3. **Product Quantization (PQ)**
4. **Inverted Files**
5. **Combinations of these techniques**

## Applications

Vector databases are used for:
- **Similarity search**
- **Semantic search**
- **Multi-modal search**
- **Recommendation engines**
- **Large Language Models (LLMs)**
- **Object detection**
- **Retrieval-Augmented Generation (RAG)**

### Retrieval-Augmented Generation (RAG)
RAG is a popular application where vector databases improve domain-specific responses of large language models:

1. Text documents are collected and processed
2. Feature vectors (embeddings) are computed for each document/section
3. Vectors are stored in the database
4. User prompts are converted to feature vectors
5. Database is queried to retrieve relevant documents
6. Retrieved documents are added to the LLM's context window
7. LLM generates responses using this enhanced context

## Popular Implementations

The vector database ecosystem includes numerous implementations with different licensing models:

### Open Source (Apache License 2.0)
- **Apache Cassandra**
- **Chroma**
- **ClickHouse**
- **LanceDB**
- **Milvus**
- **ObjectBox**
- **OpenSearch**
- **Qdrant**
- **Vespa**
- **YDB**

### Open Source (Other Licenses)
- **Elasticsearch** (Server Side Public License, Elastic License)
- **MariaDB** (GPL v2)
- **Meilisearch** (MIT License)
- **Neo4j** (GPL v3 Community Edition)
- **Postgres with pgvector** (PostgreSQL License)
- **Weaviate** (BSD 3-Clause)

### Proprietary/Managed Services
- **Aerospike**
- **Azure Cosmos DB**
- **DataStax**
- **MongoDB Atlas**
- **Oracle Database**
- **Pinecone**
- **Redis Stack**
- **Snowflake**

### Business Source License (BSL)
- **Couchbase** (BSL 1.1)
- **Lantern** (BSL 1.1)
- **SurrealDB** (BSL 1.1)

## Related Concepts

Vector databases are closely related to several important concepts in computer science and machine learning:

- **Curse of dimensionality** - Difficulties arising when analyzing high-dimensional data
- **Machine learning** - Study of algorithms that improve through experience
- **Nearest neighbor search** - Optimization problem for finding similar items
- **Recommender systems** - Systems that predict user preferences

## Key Benefits

1. **Efficient similarity search** on high-dimensional data
2. **Scalable** handling of large vector datasets
3. **Fast approximate nearest neighbor** algorithms
4. **Integration** with AI and ML workflows
5. **Support** for various data types (text, images, audio)

## Conclusion

Vector databases have become essential infrastructure for modern AI applications, particularly those involving large language models, recommendation systems, and semantic search. Their ability to efficiently store and query high-dimensional vector representations makes them crucial for applications requiring similarity search and semantic understanding.

The field continues to evolve with active research and development in similarity search algorithms, with conferences like SISAP and NeurIPS hosting competitions on vector search in large databases.

---

*Source: [Wikipedia - Vector Database](https://en.wikipedia.org/wiki/Vector_database)*  
*Summary generated on: July 28, 2025*
