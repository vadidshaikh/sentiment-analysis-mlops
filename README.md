# 🎯 Movie Review Sentiment Analyzer 

**End-to-end MLOps pipeline** — from model training to production Kubernetes deployment to full cloud teardown — built to demonstrate real-world, production-grade ML engineering practices.

> Status: ✅ Completed & Decommissioned (zero residual cloud cost)

---

## 🚀 Why This Project Stands Out

Most ML "projects" stop at a Jupyter notebook. This one goes all the way to **production infrastructure** and back — including the part most tutorials skip: **safely and completely tearing it down.**

| Capability | Demonstrated Skill |
|---|---|
| Automated CI/CD (GitHub Actions) | Build → Test → Push → Deploy, zero manual steps |
| Data & Model Versioning (DVC + S3) | Reproducible ML artifacts, no "it works on my machine" |
| Containerization (Docker) | Environment-locked, reproducible inference service |
| Container Orchestration (EKS) | Auto-healing pods behind a load balancer |
| Observability (Prometheus + Grafana) | Real production monitoring, not just print statements |
| Incident Response & Post-Mortems | Real debugging under CI failure conditions |
| Cost-Conscious Cloud Ops | Full "nuke" protocol to eliminate recurring spend |

---

## 🏗️ Architecture

```
Local Dev ──> GitHub Actions CI/CD ──> ECR (Docker Registry) ──> EKS Cluster
                     │                                              │
                     └─── DVC + S3 (model artifacts) ───────────────┘
                                                                     │
                                                        Prometheus + Grafana
                                                          (live telemetry)
```

- **Inference Engine:** FastAPI serving a Scikit-learn NLP sentiment pipeline
- **Data Lineage:** DVC-tracked model artifacts backed by S3
- **CI/CD:** GitHub Actions — test, build, push, and roll out on every merge to `main`
- **Orchestration:** Amazon EKS with auto-healing pods behind an AWS Network Load Balancer
- **Monitoring:** Prometheus scraping app metrics, visualized in Grafana

---

## 🛠️ How It Was Built (Process)

1. **Local validation first** — dependencies locked, model weights pulled via DVC, tests run with `pytest` before anything touches the cloud.
2. **Infrastructure as commands** — EKS cluster provisioned via `eksctl`, kubeconfig wired up, node health verified.
3. **Observability stood up early** — Prometheus + Grafana installed via Helm so the system was measurable from day one.
4. **CI/CD automated end-to-end** — a single GitHub Actions workflow handles dependency install, DVC pull, testing, ECR build/push, and a rolling Kubernetes deployment restart.
5. **Decommissioned responsibly** — cluster, ECR repo, S3 bucket, and any orphaned EC2 instances torn down and billing verified at $0.00.

---

## 🐛 Incidents Handled (Real Debugging, Not Just Happy Path)

This project includes a full engineering post-mortem log — the kind of documentation that separates a "script that ran once" from real ops experience:

- **`NotFittedError` on model load** → traced to a Python/scikit-learn version mismatch between training and container environments; fixed by pinning versions and aligning the base image.
- **CI pipeline dependency resolution failure** → caused by an outdated Python version in the GitHub Actions runner; fixed by aligning runner config with library requirements.
- **`pytest` collecting 0 tests** → caused by test file naming/gitignore conflicts; fixed by enforcing strict test discovery conventions.
- **Local port binding conflict** → resolved by remapping the local side of a `kubectl port-forward` tunnel.
- **Trailing post-teardown billing** → audited and confirmed a clean $0 recurring spend after cluster deletion.

---

## ✅ Project Checklist

- [x] Model trained & versioned with DVC/S3
- [x] FastAPI inference endpoint (`/predict/`)
- [x] Fully automated CI/CD to ECR + EKS
- [x] Kubernetes deployment with rolling restarts
- [x] Live Prometheus/Grafana monitoring
- [x] Full cloud teardown with $0 residual spend

---

## 📂 Tech Stack

`Python` · `FastAPI` · `Scikit-learn` · `Docker` · `DVC` · `AWS (EKS, ECR, S3, EC2)` · `GitHub Actions` · `Kubernetes` · `Helm` · `Prometheus` · `Grafana`

---

*Built to reflect the full lifecycle a production ML system actually goes through — including the parts most portfolios leave out.*
