# Comparison Table — Template

Templates LaTeX para tablas de comparación de métodos en papers de robótica.

---

## Template 1: Comparación de propiedades (cualitativa)

Usa cuando comparas si distintos métodos soportan o no ciertas propiedades.

```latex
\begin{table}[t]
\centering
\caption{Comparison of related methods. \cmark = supported, \xmark = not supported, $\sim$ = partially.}
\label{tab:comparison}
\setlength{\tabcolsep}{4pt}
\begin{tabular}{lcccccc}
\toprule
\multirow{2}{*}{Method} & Real & No & Low & Multi- & \multirow{2}{*}{Venue} \\
                        & Robot & Demo & Data & Task &  \\
\midrule
Method A~\cite{refA}  & \cmark & \xmark & \xmark & \xmark & ICRA'22 \\
Method B~\cite{refB}  & \xmark & \cmark & \cmark & \xmark & CoRL'23 \\
Method C~\cite{refC}  & \cmark & $\sim$ & \xmark & \cmark & IROS'23 \\
\midrule
\textbf{Ours}          & \cmark & \cmark & \cmark & \cmark & -- \\
\bottomrule
\end{tabular}
\end{table}
```

*Requiere en el preámbulo:*
```latex
\usepackage{pifont}
\newcommand{\cmark}{\ding{51}}
\newcommand{\xmark}{\ding{55}}
\usepackage{multirow}
\usepackage{booktabs}
```

---

## Template 2: Comparación cuantitativa de resultados

Usa para comparar métricas numéricas entre métodos en distintas tareas.

```latex
\begin{table}[t]
\centering
\caption{
  Quantitative comparison on \textit{TaskName} benchmark.
  We report \textit{métrica} (mean $\pm$ std over $N$ runs).
  Best results in \textbf{bold}, second-best \underline{underlined}.
}
\label{tab:results}
\begin{tabular}{lcccc}
\toprule
              & \multicolumn{2}{c}{Easy} & \multicolumn{2}{c}{Hard} \\
\cmidrule(lr){2-3}\cmidrule(lr){4-5}
Method        & SR (\%) & ATE (m) & SR (\%) & ATE (m) \\
\midrule
BC~\cite{bc}               & $62.3 \pm 4.1$ & $0.08$ & $31.4 \pm 5.2$ & $0.14$ \\
GAIL~\cite{gail}           & $71.5 \pm 3.8$ & $0.06$ & $44.2 \pm 4.9$ & $0.11$ \\
Method C~\cite{methodC}    & \underline{$78.2 \pm 3.1$} & \underline{$0.05$} & \underline{$52.1 \pm 4.1$} & \underline{$0.09$} \\
\midrule
\textbf{Ours} & $\mathbf{86.4 \pm 2.7}$ & $\mathbf{0.04}$ & $\mathbf{63.8 \pm 3.5}$ & $\mathbf{0.07}$ \\
\bottomrule
\end{tabular}
\end{table}
```

---

## Template 3: Ablation study

```latex
\begin{table}[t]
\centering
\caption{
  Ablation study on [tarea/benchmark].
  Each row removes one component of our full method.
  SR = success rate (\%), averaged over $N$ trials.
}
\label{tab:ablation}
\begin{tabular}{lcc}
\toprule
Variant              & SR (\%) & $\Delta$ \\
\midrule
Full method (ours)   & $\mathbf{86.4}$ & -- \\
w/o Component A      & $74.1$ & $-12.3$ \\
w/o Component B      & $71.8$ & $-14.6$ \\
w/o Component A+B    & $63.2$ & $-23.2$ \\
\midrule
Baseline~\cite{ref}  & $62.3$ & $-24.1$ \\
\bottomrule
\end{tabular}
\end{table}
```

---

## Template 4: Comparación multi-tarea

```latex
\begin{table*}[t]
\centering
\caption{
  Performance across [N] manipulation tasks.
  Values are success rates (\%) $\pm$ std over [N] trials per task.
  $\dagger$ = methods evaluated in simulation only.
}
\label{tab:multitask}
\begin{tabular}{lccccccc}
\toprule
Method & Task 1 & Task 2 & Task 3 & Task 4 & Task 5 & Task 6 & Mean \\
\midrule
Method A$\dagger$~\cite{refA} & $55.0$ & $48.2$ & $61.3$ & $43.1$ & $38.7$ & $52.4$ & $49.8$ \\
Method B~\cite{refB}          & $68.3$ & $59.1$ & $70.4$ & $55.2$ & $47.6$ & $63.1$ & $60.6$ \\
\midrule
\textbf{Ours}                  & $\mathbf{81.2}$ & $\mathbf{74.3}$ & $\mathbf{83.5}$ & $\mathbf{69.4}$ & $\mathbf{62.8}$ & $\mathbf{77.1}$ & $\mathbf{74.7}$ \\
\bottomrule
\end{tabular}
\end{table*}
```

---

## Guía para elegir propiedades de comparación

Las propiedades de la tabla de comparación deben ser:
1. **Relevantes** para la contribución del paper (no agregas propiedades solo para que "ours" gane)
2. **Verificables** en los papers comparados (si no puedes confirmar en el paper original, no lo claims)
3. **Binarias o métricas** — evitar propiedades subjetivas
4. **Limitadas** — 4-6 propiedades máximo para legibilidad

**Propiedades comunes en robótica:**

| Área | Propiedades típicas |
|------|-------------------|
| Imitation learning | Real robot demos, zero-shot transfer, multi-task, low-data |
| Manipulation | Contact-rich, deformable objects, in-hand, bimanual |
| Navigation | Mapless, long-horizon, dynamic obstacles, outdoor |
| Sim2real | Domain randomization, adaptation at test time, hardware-agnostic |
| Humanoids | Loco-manipulation, whole-body, teleoperation, zero-shot |
