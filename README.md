Architecture
                    
                    
                    ┌──────────────────────┐
                    │        USER          │
                    └──────────┬───────────┘
                               │
                    ┌──────────▼───────────┐
                    │   INPUT SELECTION    │
                    │                      │
                    │  1 → Voice Input     │
                    │  2 → Text Input      │
                    └──────────┬───────────┘
                               │
                ┌──────────────▼──────────────┐
                │      INPUT PROCESSING       │
                │                             │
                │  lowercase                  │
                │  special-character removal  │
                │  split into words           │
                └──────────────┬──────────────┘
                               │
                ┌──────────────▼──────────────┐
                │      NLP KEYWORD FILTER     │
                │                             │
                │       check_in()            │
                │       check_out()           │
                └──────────────┬──────────────┘
                               │
                     ┌─────────▼─────────┐
                     │ Generate two keys │
                     │                   │
                     │ key               │
                     │ key1              │
                     └─────────┬─────────┘
                               │
              ┌────────────────▼────────────────┐
              │       EXACT / RULE MATCHING    │
              │                                │
              │ project estimation             │
              │ labour requirement             │
              │ material types                 │
              │ ...                            │
              │ purchase order management      │
              │                                │
              │      40 predefined intents     │
              └────────────────┬────────────────┘
                               │
                       Match found?
                      ┌────────┴────────┐
                     YES               NO
                      │                 │
                      ▼                 ▼
              ┌──────────────┐   ┌─────────────────────┐
              │ Question ID  │   │ Keyword-based       │
              │   selected   │   │ fallback matching   │
              └──────┬───────┘   └──────────┬──────────┘
                     │                      │
                     │              Match found?
                     │             ┌────────┴────────┐
                     │            YES               NO
                     │             │                 │
                     │             ▼                 ▼
                     │      ┌──────────────┐  ┌─────────────────┐
                     │      │ Question ID  │  │ FUZZY MATCHING  │
                     │      └──────┬───────┘  │                 │
                     │             │          │ fuzz.WRatio()  │
                     │             │          │ 40 comparisons  │
                     │             │          └───────┬─────────┘
                     │             │                  │
                     │             │            Score >= 90?
                     │             │             ┌────┴────┐
                     │             │            YES       NO
                     │             │             │         │
                     │             │             ▼         ▼
                     │             │      ┌───────────┐ ┌─────────────┐
                     │             │      │Question ID│ │  FALLBACK   │
                     │             │      └─────┬─────┘ │             │
                     │             │            │       │ back_track  │
                     │             │            │       │ unanswered  │
                     │             │            │       └─────────────┘
                     └─────────────┴────────────┘
                                   │
                         ┌─────────▼──────────┐
                         │  ANSWER RETRIEVAL  │
                         │                    │
                         │ get_answers()      │
                         │                    │
                         │ Construction_150_  │
                         │ Answers_Converted  │
                         └─────────┬──────────┘
                                   │
                         ┌─────────▼──────────┐
                         │  DISPLAY ANSWER    │
                         │                    │
                         │ Question title     │
                         │ Answer             │
                         └────────────────────┘
