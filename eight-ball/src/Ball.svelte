<script>
  export let answer;
  export let isShaking;
  import { fade } from "svelte/transition";
</script>

<div class="ball">
  <div class="window">
    <div class="triangle">
      <p class="text">
        {answer}
      </p>
    </div>
    <div class="shadow" />
    {#if !answer || isShaking}
      <div transition:fade class="overlay" />
    {/if}
  </div>
</div>

<style>
  .ball {
    width: 500px;
    height: 500px;
    border-radius: 50%;
    background-color: black;
    display: flex;
    justify-content: center;
    align-items: center;
    background: radial-gradient(circle at 30% 30%, #333, #000);
  }
  .window {
    width: 200px;
    height: 200px;
    border-radius: 50%;
    background-color: black;
    position: relative;
  }

  .triangle {
    width: 0;
    height: 0;
    border-left: 70px solid transparent;
    border-right: 70px solid transparent;
    border-top: 100px solid blue;
    position: absolute;
    top: 50px;
    left: 30px;
    font-family: sans-serif;
    font-variant: small-caps;
    animation: floating 6s linear infinite;
  }

  .shadow {
    z-index: 1;
    position: absolute;
    border-radius: 50%;
    width: 200px;
    height: 200px;
    background: linear-gradient(to left, rgba(0, 0, 0, 0.9), rgba(0, 0, 0, 0));
    animation: rotating 6s infinite linear;
  }

  .overlay {
    z-index: 10;
    position: absolute;
    border-radius: 50%;
    width: 200px;
    height: 200px;
    background-color: black;
  }
  .text {
    position: absolute;
    top: -100px;
    left: -28px;
    font-size: 12px;
    width: 60px;
    text-align: center;
    font-family: sans-serif;
    font-variant: small-caps;
    color: white;
  }

  @keyframes shake {
    0% {
      transform: rotate(1deg) translate(3px, 4px);
    }
    5% {
      transform: rotate(2deg) translate(-4px, -1px);
    }
    10% {
      transform: rotate(0deg) translate(0px, -5px);
    }
    15% {
      transform: rotate(2deg) translate(4px, 0px);
    }
    20% {
      transform: rotate(1deg) translate(-3px, 3px);
    }
    25% {
      transform: rotate(4deg) translate(4px, -3px);
    }
    30% {
      transform: rotate(1deg) translate(3px, -5px);
    }
    35% {
      transform: rotate(-2deg) translate(3px, 4px);
    }
    40% {
      transform: rotate(0deg) translate(-3px, -3px);
    }
    45% {
      transform: rotate(-1deg) translate(4px, 4px);
    }
    50% {
      transform: rotate(1deg) translate(-4px, 3px);
    }
    55% {
      transform: rotate(2deg) translate(-4px, -1px);
    }
    60% {
      transform: rotate(0deg) translate(0px, -5px);
    }
    65% {
      transform: rotate(2deg) translate(4px, 0px);
    }
    70% {
      transform: rotate(1deg) translate(-3px, 3px);
    }
    75% {
      transform: rotate(4deg) translate(4px, -3px);
    }
    80% {
      transform: rotate(1deg) translate(3px, -5px);
    }
    85% {
      transform: rotate(1deg) translate(1px, -2px);
    }
    100% {
      transform: rotate(0deg) translate(0px, 0px);
    }
  }
  .shake {
    animation: shake 1.2s ease-out 2;
  }

  /* Triangle gently floating around */
  @keyframes floating {
    from {
      transform: rotateZ(0) rotateY(15deg) translateZ(50px) rotateZ(0);
    }
    to {
      transform: rotateZ(1turn) rotateY(15deg) translateZ(50px) rotateZ(-1turn);
    }
  }

  /* Roatating shadow */
  @keyframes rotating {
    to {
      transform: rotate(1turn);
    }
  }
</style>
