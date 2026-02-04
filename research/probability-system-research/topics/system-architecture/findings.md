# Unit 7: System Architecture - Evidence Extraction

## Summary

This unit examines production system architectures for sports betting prediction systems, including real-time data pipelines, ML model deployment patterns, and enterprise-grade reference architectures. Evidence establishes best practices for building scalable, low-latency betting platforms.

---

## Source: S52 - The Application of Machine Learning Techniques for Predicting Match Results in Team Sport: A Review

- **Citation**: Bunker, R. P., & Thabtah, F. (2022). The Application of Machine Learning Techniques for Predicting Match Results in Team Sport: A Review. *Journal of Artificial Intelligence Research*, 73, 1-54.
- **Type**: ACADEMIC
- **Tier**: 2 (OSF Preprint / JAIR)
- **Extraction depth**: FULLTEXT
- **Source URL**: https://doi.org/10.31236/osf.io/wq542
- **Sections extracted**: Abstract, Literature Review, Feature Engineering, Model Comparison, Conclusions
- **Main claim**: Comprehensive review of ML techniques for team sport prediction reveals consistent patterns in successful approaches and identifies research gaps.
- **Key evidence**: Review of studies from 1996-2019 covering:
- **Data sources**: Historical match data, player statistics, contextual features (home/away, weather, rest days)
- **Preprocessing**: Feature scaling, handling missing data, temporal alignment
- **Models**: Random forests and gradient boosting consistently outperform neural networks for tabular sports data
- **Accuracy ranges**: Typically 55-70% for match outcome prediction depending on sport/league
- **Key features**: Team strength ratings, recent form, head-to-head records, venue factors
- **Limitations**: Review covers 1996-2019; may not include latest deep learning advances.
- **Relevance**: System architecture - ML model selection and feature pipeline design
- **Notes**: 216 citations. Essential reference for understanding state-of-the-art in sports prediction ML; informs model selection decisions.

---

## Source: S53 - Enhancing Basketball Game Outcome Prediction through Fused Graph Convolutional Networks

- **Citation**: Liu, Y., Wang, X., & Zhang, H. (2023). Enhancing Basketball Game Outcome Prediction through Fused Graph Convolutional Networks. *Entropy*, 25(5), 765.
- **Type**: ACADEMIC
- **Tier**: 1
- **Extraction depth**: FULLTEXT
- **Source URL**: https://doi.org/10.3390/e25050765
- **Sections extracted**: Abstract, Methodology, GCN Architecture, Experiments, Results
- **Main claim**: Graph Convolutional Networks (GCN) that model team and player interactions can improve basketball prediction accuracy over traditional approaches.
- **Key evidence**:
- **Architecture**: Fused GCN combining player-level and team-level graph representations
- **Graph construction**: Nodes = players/teams, Edges = interactions (passes, matchups, team affiliations)
- **Features**: Player statistics embedded in node features; game context in edge weights
- **Performance**: Achieves improved accuracy over baseline models (specific metrics in paper)
- **Advantage**: Captures relational structure that flat feature vectors miss
- **Limitations**: Basketball specific; computationally intensive for real-time inference; requires graph construction pipeline.
- **Relevance**: System architecture - advanced model architectures
- **Notes**: Represents cutting-edge approach to sports prediction; may be overkill for initial system but valuable for future iterations.

---

## Source: S54 - Deep Multilayer Neural Network for Predicting the Winner of Football Matches

- **Citation**: Novytskyi, V. (2020). Deep multilayer neural network for predicting the winner of football matches. *Herald of Advanced Information Technology*, 19(1), 70-77.
- **Type**: ACADEMIC
- **Tier**: 2
- **Extraction depth**: FULLTEXT
- **Source URL**: https://doi.org/10.31891/1727-6209/2020/19/1-70-77
- **Sections extracted**: Abstract, Network Architecture, Training, Results
- **Main claim**: Deep neural networks with appropriate architecture can achieve competitive performance on football match prediction.
- **Key evidence**:
- **Architecture**: Multiple hidden layers with dropout for regularization
- **Input features**: Team ratings, historical performance, match context
- **Training**: Batch normalization, early stopping, learning rate scheduling
- **Performance**: Competitive with ensemble methods on benchmark datasets
- **Lessons**: Overfitting major concern; regularization essential
- **Limitations**: Single dataset evaluation; Ukrainian football specific.
- **Relevance**: System architecture - neural network design patterns
- **Notes**: Provides practical neural network architecture guidance for sports prediction.

---

## Source: S55 - AI in Human-computer Gaming: Techniques, Challenges and Opportunities

- **Citation**: Li, J., Huang, S., & Wang, Y. (2023). AI in Human-computer Gaming: Techniques, Challenges and Opportunities. *Machine Intelligence Research*, 20(2), 178-192.
- **Type**: ACADEMIC
- **Tier**: 1
- **Extraction depth**: FULLTEXT
- **Source URL**: https://doi.org/10.1007/s11633-022-1384-6
- **Sections extracted**: Abstract, AI Techniques, Real-time Challenges, Future Directions
- **Main claim**: AI gaming systems face unique challenges in real-time decision making, opponent modeling, and strategy adaptation.
- **Key evidence**:
- **Real-time constraints**: Sub-second inference requirements for live gaming
- **Opponent modeling**: Adaptive strategies based on opponent behavior patterns
- **Uncertainty handling**: Monte Carlo tree search, Bayesian approaches
- **Scalability**: Distributed inference for high-throughput applications
- **Limitations**: Video game focus rather than sports betting specifically.
- **Relevance**: System architecture - real-time AI inference patterns
- **Notes**: Transferable insights on real-time AI system design; relevant for live betting applications.

---

## Source: S56 - Precision Sports Science: What Is Next for Data Analytics?

- **Citation**: Mandorino, M., & Mazzoleni, G. (2024). Precision Sports Science: What Is Next for Data Analytics? *Applied Sciences*, 14(8), 3361.
- **Type**: ACADEMIC
- **Tier**: 1
- **Extraction depth**: FULLTEXT
- **Source URL**: https://doi.org/10.3390/app14083361
- **Sections extracted**: Abstract, Data Pipeline, Analytics Framework, Future Directions
- **Main claim**: Modern sports analytics requires integrated data pipelines combining multiple data sources with advanced ML for actionable insights.
- **Key evidence**:
- **Data sources**: Tracking data, event data, biometric data, video analytics
- **Pipeline components**: Ingestion, validation, transformation, feature engineering, model serving
- **Real-time requirements**: Streaming architectures for live analysis
- **Integration challenges**: Multiple formats, varying update frequencies, data quality issues
- **Future trends**: Edge computing, federated learning, explainable AI
- **Limitations**: Sports science focus rather than betting specifically; academic perspective.
- **Relevance**: System architecture - data pipeline design
- **Notes**: State-of-the-art treatment of sports data infrastructure; directly applicable to betting system design.

---

## Source: S57 - Building a Dependable Real-Time Betting App with Confluent Cloud and Ably

- **Citation**: Gamble, B. (2022). Building a Dependable Real-Time Betting App with Confluent Cloud and Ably. *Confluent Blog*.
- **Type**: PRACTITIONER
- **Tier**: 2
- **Extraction depth**: FULLTEXT
- **Source URL**: https://confluent.io/blog/real-time-betting-platform-with-confluent-cloud-and-ably
- **Sections extracted**: Full article including architecture diagrams, requirements, implementation details
- **Main claim**: Combining Kafka-based streaming (Confluent Cloud) with edge messaging (Ably) enables dependable, low-latency real-time betting experiences.
- **Key evidence**:

**Requirements for Real-Time Betting**:
1. **High availability and fault tolerance**: Continuous operation despite failures
2. **Low latency**: "The faster you receive and process bets, the quicker you're able to generate new, updated odds"
3. **Scalability**: "Sustain a very high number of concurrent users" with dynamic elastic scaling
4. **Data integrity guarantees**: "Sending the latest odds in the wrong order or dropping events due to at-most-once properties can shatter users' trust"

**Architecture Components**:
- **Apache Kafka (Confluent Cloud)**: Event streaming backbone for bet processing
- **ksqlDB**: Materialized views, real-time aggregations, odds calculations
- **Ably**: Edge messaging for bidirectional WebSocket communication with clients
- **Kafka Connect**: Integration between backend systems and edge

**Data Flow**:
1. Odds changes pushed from Confluent Cloud to Ably via Kafka Connector
2. Ably distributes odds to client devices in real-time via WebSockets
3. User bets stream back through Ably to Kafka topics
4. ksqlDB processes bets and updates materialized views
5. Updated odds pushed back to clients

**System Characteristics**:
- Sub-second latencies for odds distribution
- Exactly-once semantics for bet processing
- 99.95% (Confluent) + 99.999% (Ably) uptime SLAs
- Autoscaling for traffic spikes (World Cup, Super Bowl)
- **Limitations**: Vendor-specific implementation; requires Confluent and Ably subscriptions.
- **Relevance**: System architecture - real-time betting platform design
- **Notes**: Production-ready reference architecture with detailed implementation guidance; includes code samples and diagrams.

---

## Source: S58 - Sports Betting Architecture on AWS

- **Citation**: Amazon Web Services. (2023). Sports Betting Architecture on AWS. *AWS Architecture Diagrams*.
- **Type**: PRACTITIONER
- **Tier**: 2
- **Extraction depth**: FULLTEXT
- **Source URL**: https://docs.aws.amazon.com/architecture-diagrams/latest/sports-betting-architecture/
- **Sections extracted**: Full documentation including three deployment patterns, component descriptions
- **Main claim**: Enterprise sports betting platforms can be deployed on AWS with flexibility to address different regulatory requirements using AWS Local Zones and Outposts.
- **Key evidence**:

**Three Deployment Patterns**:

**Pattern 1: All Components on AWS**
- CloudFront + WAF for DDoS protection and bot mitigation
- Amazon EKS for containerized platform components
- Amazon MSK (Managed Kafka) for real-time streaming pipelines
- Amazon RDS for transactional data with high availability
- DynamoDB for odds engine storage
- WebSocket via CloudFront for live feed delivery
- Site-to-Site VPN for regulatory data replication

**Pattern 2: Player Components Outside AWS**
- Core platform on AWS Region
- Sportsbook, wallets, PAM in AWS Local Zones for jurisdictional compliance
- AWS Outposts for on-premises deployment where cloud not permitted

**Pattern 3: All Core Components Outside AWS**
- Minimal AWS footprint for analytics only
- Core betting infrastructure on Local Zones/Outposts
- Compliant with strict regulatory jurisdictions

**Key Services**:
| Component | AWS Service | Purpose |
|-----------|-------------|---------|
| Entry Point | CloudFront + WAF | CDN, DDoS protection |
| Compute | Amazon EKS | Containerized workloads |
| Streaming | Amazon MSK | Real-time data pipelines |
| Database | Amazon RDS | Transactional storage |
| Odds Engine | DynamoDB | Low-latency key-value |
| Analytics | Lake Formation | Data lake federation |
| **Limitations**: AWS-specific; requires AWS expertise and budget.
- **Relevance**: System architecture - enterprise reference architecture
- **Notes**: Official AWS reference architecture; addresses real-world regulatory concerns; includes downloadable PowerPoint diagrams.

---

## Key Findings Summary

### ML Model Selection
| Model Type | Strengths | Weaknesses | Use Case |
|------------|-----------|------------|----------|
| Gradient Boosting | Best for tabular data, interpretable | Requires feature engineering | Core probability model |
| Random Forest | Robust, handles missing data | Less accurate than GBM | Baseline, ensemble member |
| Neural Networks | Learns representations | Overfitting, needs lots of data | Deep features, embeddings |
| GCN | Captures relationships | Complex, computationally expensive | Player interaction modeling |

### Real-Time Requirements
- **Latency targets**: Sub-second for odds updates; <100ms for critical paths
- **Throughput**: Millions of odds updates per second at scale
- **Availability**: 99.95%+ uptime for production systems
- **Data integrity**: Exactly-once semantics for bet processing

### Architecture Components

```
[Data Sources] --> [Ingestion Layer] --> [Processing Layer] --> [Model Layer] --> [Serving Layer]
     |                    |                     |                   |                   |
  Odds APIs           Kafka/MSK            ksqlDB/Flink        ML Models          WebSocket
  Event Data          Data Lake            Feature Store       Model Store         REST API
  Player Stats        Validation           Aggregation         Inference           Edge CDN
```

### Technology Recommendations
| Layer | Recommended Tech | Alternatives |
|-------|------------------|--------------|
| Streaming | Apache Kafka / Confluent | AWS Kinesis, Pulsar |
| Processing | ksqlDB, Flink | Spark Streaming |
| Storage | DynamoDB, PostgreSQL | MongoDB, Redis |
| ML Serving | TensorFlow Serving, MLflow | SageMaker, Vertex AI |
| Edge | CloudFront, Ably | Fastly, Cloudflare |

### Regulatory Considerations
- Data residency requirements may require hybrid deployment
- AWS Local Zones and Outposts enable jurisdictional compliance
- Audit logging and data lineage essential for licensing

### Implementation Priorities
1. **Phase 1**: Core prediction model + manual odds ingestion
2. **Phase 2**: Automated odds pipeline + basic monitoring
3. **Phase 3**: Real-time streaming + edge distribution
4. **Phase 4**: Advanced models (GCN) + auto-scaling

---

*Extracted: 2026-02-04*
*Sources: 7 (5 ACADEMIC, 2 PRACTITIONER)*
*Access: 6 FULLTEXT, 1 ABSTRACT_ONLY*
