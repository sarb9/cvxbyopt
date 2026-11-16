<h1 align="center">
  Adversarial Bandit Convex Optimization<br>
  with <i>d</i><sup>3/2</sup>√<i>n</i> Regret
</h1>

<p align="center">
  <a href="adversarial/advcvx.pdf"><img src="https://img.shields.io/badge/Read_the_paper-PDF-2563eb?style=for-the-badge" alt="Read the paper (PDF)"></a>
  <a href="adversarial/advcvx.tex"><img src="https://img.shields.io/badge/LaTeX-Source-475569?style=for-the-badge" alt="LaTeX source"></a>
</p>

## Abstract

We study adversarial bandit convex optimization, where in each of <i>n</i> rounds a learner chooses a point <i>A</i><sub><i>t</i></sub> in a convex body 𝒦 ⊂ ℝ<sup><i>d</i></sup> and observes only a noisy value of a convex loss <i>f</i><sub><i>t</i></sub>: 𝒦 → [0, 1] at that point. The losses are chosen by an adversary, who may change them from round to round and adapt them to the learner's past actions.

We improve the best known regret bound for this problem from Õ(<i>d</i><sup>5/2</sup>√<i>n</i>) ([Lattimore, 2020](https://doi.org/10.4171/MSL/17); [Lattimore, 2026](https://doi.org/10.1017/9781009607551)) to Õ(<i>d</i><sup>3/2</sup>√<i>n</i>), which matches the rate conjectured by [Bubeck et al. (2017)](https://doi.org/10.1145/3055399.3055403). Together with the recent lower bound of Ω(<i>d</i><sup>4/3</sup>√<i>n</i>) due to [Rajaraman and Han (2026)](https://arxiv.org/abs/2607.18652v3), it determines the minimax regret up to a factor of <i>d</i><sup>1/6</sup> and logarithmic factors.

The algorithm is an online Newton step with Gaussian exploration. Unlike earlier methods of this kind, it uses unbiased estimates of the gradient and Hessian of the Gaussian smoothing of the loss, rather than of an optimistic surrogate.
