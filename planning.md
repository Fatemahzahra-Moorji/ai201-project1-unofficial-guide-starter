# Project 1 Planning: The Unofficial Guide

> Write this document before you write any pipeline code.
> Your spec and architecture diagram are what you'll use to direct AI tools (Claude, Copilot, etc.) to generate your implementation — the more specific they are, the more useful the generated code will be.
> Update the Retrieval Approach and Chunking Strategy sections if you change your approach during implementation.
> Update this file before starting any stretch features.

---

## Domain

<!-- What domain did you choose? Why is this knowledge valuable and hard to find through official channels? -->
The domain I chose is Student Reviews of Biology Professors and Courses. This system makes student-generated knowledge about biology professors and courses searchable and answerable. Students share this kind of knowledge on Rate My Professors, Reddit, and course-specific forums, but it's scattered across dozens of pages with no way to ask a plain question like "Which bio professor is best for pre-med students?" or "Is BIO 301 worth taking if you struggle with labs?" Official channels like course catalogs and department websites tell you what a course covers, not what it's actually like to take it. 

---

## Documents

<!-- List your specific sources: URLs, subreddit names, forum threads, or file descriptions.
     Aim for at least 10 sources that together cover different subtopics or perspectives within your domain. -->

| # | Source | Description | URL or location |
|---|--------|-------------|-----------------|
| 1 | Rate My Professors | Student reviews of a bio professor (intro bio) | https://www.ratemyprofessors.com/professor/1751109 |
| 2 | Rate My Professors | Student reviews of a bio professor (upper level courses) | https://www.ratemyprofessors.com/professor/889023 |
| 3 | Rate My Professors | Student reviews of a third bio professor | https://www.ratemyprofessors.com/professor/823707 |
| 4 | Reddit r/AdelphiUniversity | Student advice on suitability of Adelphi for premed |https://www.reddit.com/r/AdelphiUniversity/comments/1jsf5li/which_school_should_i_pick/|
| 5 | Reddit r/premed | Student guide for undergrad premed | https://www.reddit.com/r/premed/wiki/coursework/ |
| 6 | Reddit r/premed | Tips for excelling in Bio courses | https://www.reddit.com/r/premed/comments/y0l51b/some_advice_if_you_struggle_with_bio_classes/ |
| 7 | Reddit r/biology | General biology course survival tips | https://www.reddit.com/r/biology/comments/ps6hkz/how_to_study_for_biology/ |
| 8 | StudentDoctor Network | Cell Biology vs. Genetics | https://forums.studentdoctor.net/threads/cell-biology-vs-genetics.1200034/ |
| 9 | Rate My Professors | Student reviews of a bio lab professor | https://www.ratemyprofessors.com/professor/219596 |
| 10 | StudentDoctor Network | Clarity on Biology Course Sequence for Pre-Requisites | https://forums.studentdoctor.net/threads/clarity-on-biology-course-sequence-for-pre-requisites.1468738/ |

---

## Chunking Strategy

<!-- How will you split documents into chunks?
     State your chunk size (in tokens or characters), overlap size, and explain why those
     numbers fit the structure of your documents.
     A review-heavy corpus warrants different chunking than a long FAQ. -->

**Chunk size:**

**Overlap:**

**Reasoning:**

---

## Retrieval Approach

<!-- Which embedding model are you using (e.g., all-MiniLM-L6-v2 via sentence-transformers)?
     How many chunks will you retrieve per query (top-k)?
     If you were deploying this for real users and cost wasn't a constraint, what tradeoffs
     would you weigh in choosing a different embedding model — context length, multilingual
     support, accuracy on domain-specific text, latency? -->

**Embedding model:**

**Top-k:**

**Production tradeoff reflection:**

---

## Evaluation Plan

<!-- List your 5 test questions with their expected correct answers.
     Questions should be specific enough that you can judge whether the system's response
     is right or wrong. "What are good dining halls?" is too vague.
     "What do students say about wait times at [dining hall name] during lunch?" is testable. -->

| # | Question | Expected answer |
|---|----------|-----------------|
| 1 | | |
| 2 | | |
| 3 | | |
| 4 | | |
| 5 | | |

---

## Anticipated Challenges

<!-- What could go wrong? Name at least two specific risks with reasoning.
     Consider: noisy or inconsistent documents, missing source attribution, off-topic
     retrieval, chunks that split key information across boundaries. -->

1.

2.

---

## Architecture

<!-- Draw a diagram of your pipeline showing the five stages:
     Document Ingestion → Chunking → Embedding + Vector Store → Retrieval → Generation
     Label each stage with the tool or library you're using.
     You can use ASCII art, a Mermaid diagram, or embed a sketch as an image.
     You'll use this diagram as context when prompting AI tools to implement each stage. -->

---

## AI Tool Plan

<!-- For each part of the pipeline below, describe:
     - Which AI tool you plan to use (Claude, Copilot, ChatGPT, etc.)
     - What you'll give it as input (which sections of this planning.md, which requirements)
     - What you expect it to produce
     - How you'll verify the output matches your spec

     "I'll use AI to help me code" is not a plan.
     "I'll give Claude my Chunking Strategy section and ask it to implement chunk_text()
     with my specified chunk size and overlap" is a plan. -->

**Milestone 3 — Ingestion and chunking:**

**Milestone 4 — Embedding and retrieval:**

**Milestone 5 — Generation and interface:**
