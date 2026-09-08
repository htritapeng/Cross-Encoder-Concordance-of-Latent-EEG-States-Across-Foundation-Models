# How to use GitHub for this ISDS publication

This guide assumes the package is already on your PC at:

`C:\Users\htpeng2\Desktop\Rita_research\Lab\data_related\EEG\Nhat\ISDS\Github`

Goal: put this folder on **GitHub.com** so reviewers, coauthors, and readers can open figures, code, and the response letter from a stable URL you can put in the camera-ready paper.

---

## 1. Why GitHub for a paper?

| Use | Example |
|-----|---------|
| **Reproducibility** | Link in paper: “Code and figures: https://github.com/YOU/isds-2026-eeg-concordance” |
| **Supplementary artifacts** | Occupancy exports, WCSS metrics, paper figures |
| **Version freeze** | Tag `v1.0-camera-ready` so the snapshot matches the published PDF |
| **Coauthor sync** | Push/pull instead of emailing zip files |

GitHub ≠ Google Drive. It tracks **versions** (commits). Prefer small text + figures; keep huge EEG arrays elsewhere (Zenodo / lab storage) and link them.

---

## 2. One-time setup

### A. Create a GitHub account
1. Go to [https://github.com/signup](https://github.com/signup)
2. Use your institutional email if possible

### B. Install tools (pick one path)

**Recommended on this Windows PC (Git CLI is not installed yet):**  
install **[GitHub Desktop](https://desktop.github.com/)**, sign in, then use File → Add local repository (see §4).

**Or install Git CLI:**
1. Download: [https://git-scm.com/download/win](https://git-scm.com/download/win)
2. Close and reopen PowerShell, then check:

```powershell
git --version
```

```powershell
git config --global user.name "Rita Huan-Ting Peng"
git config --global user.email "your.email@university.edu"
```

**Authenticate (if using CLI):** [GitHub CLI](https://cli.github.com/) (`gh auth login`), or HTTPS + Personal Access Token when `git push` asks for a password.

---

## 3. Create an empty repository on GitHub.com

1. Click **+ → New repository**
2. Suggested name: `isds-2026-eeg-concordance` (or similar)
3. Description: `ISDS 2026 Paper 4217 — cross-encoder latent EEG state concordance (TUEP)`
4. Visibility:
   - **Private** until camera-ready / copyright is clear, then make **Public**
   - Or **Public** now if coauthors agree
5. **Do not** add a README / .gitignore / license on the website (this folder already has them)
6. Click **Create repository**
7. Copy the repo URL, e.g. `https://github.com/YOURUSER/isds-2026-eeg-concordance.git`

---

## 4. Push this folder (first time)

Open PowerShell:

```powershell
cd "C:\Users\htpeng2\Desktop\Rita_research\Lab\data_related\EEG\Nhat\ISDS\Github"

git init -b main
git add .
git status
git commit -m "Initial camera-ready package for ISDS 2026 Paper 4217"

git remote add origin https://github.com/YOURUSER/isds-2026-eeg-concordance.git
git push -u origin main
```

If `git push` asks for credentials, use a **Personal Access Token** (GitHub → Settings → Developer settings → Tokens), not your GitHub password.

### Using GitHub Desktop instead
1. File → Add local repository → select the `Github` folder  
2. Publish repository → choose name/visibility → Publish  

---

## 5. Everyday workflow (after the first push)

```powershell
cd "C:\Users\htpeng2\Desktop\Rita_research\Lab\data_related\EEG\Nhat\ISDS\Github"

# after you change files:
git add .
git commit -m "Update response letter and WCSS figure"
git push
```

Tips:
- Commit messages should say **why** (e.g. “Add PCA co-assignment figure for circularity response”)
- Pull before you start if a coauthor also pushes: `git pull`

---

## 6. Freeze the camera-ready version (recommended)

When the PDF is final:

```powershell
git tag -a v1.0-camera-ready -m "ISDS 2026 Paper 4217 camera-ready"
git push origin v1.0-camera-ready
```

On GitHub: **Releases → Draft a new release → choose tag `v1.0-camera-ready`**  
Attach the camera-ready PDF if allowed by Springer.

In the paper, write something like:

> Code and supplementary figures are available at  
> `https://github.com/YOURUSER/isds-2026-eeg-concordance`  
> (tag `v1.0-camera-ready`).

---

## 7. What to put in the paper / submission portal

1. **GitHub URL** in a “Code availability” / “Supplementary material” sentence  
2. Optional: **DOI** later via Zenodo (“Cite this repository” → archive)  
3. Do **not** upload raw patient EEG to a public repo unless TUEP license and IRB allow it (this package intentionally omits raw EEG)

---

## 8. Good practices for publication repos

| Do | Don’t |
|----|-------|
| Small CSVs/JSONs + figures + scripts | Commit multi-GB `.npy` / raw EDF |
| `requirements.txt` + short README | Hard-code only your `C:\Users\...` paths in demos |
| Tag a release matching the PDF | Force-push `main` after coauthors pull |
| Private → Public when ready | Commit passwords, tokens, `.env` |

Scripts under `code/` may still contain original absolute paths from the lab machine. For a quick local check, use:

```powershell
python code/hungarian_alignment_demo.py
```

which reads packaged data under `data/occupancy/`.

---

## 9. Checklist for ISDS camera-ready

- [ ] Repo created and `main` pushed  
- [ ] README shows paper title, authors, venue  
- [ ] Main figures visible in `figures/`  
- [ ] Demo runs: `python code/hungarian_alignment_demo.py`  
- [ ] Tag `v1.0-camera-ready` after final PDF  
- [ ] URL added to camera-ready manuscript if required  
- [ ] Coauthors can access the repo (Settings → Collaborators)

---

## 10. Need help?

- GitHub Docs: [https://docs.github.com/en/get-started](https://docs.github.com/en/get-started)  
- Hello World: [https://guides.github.com/activities/hello-world/](https://guides.github.com/activities/hello-world/)  

If you want, an AI assistant can run the first `git init` / commit locally; **creating the empty repo on github.com and `git push` usually need your login**.
