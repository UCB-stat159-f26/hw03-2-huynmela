import matplotlib.pyplot as plt
import numpy as np

def match_age_results(ax, player):
    age_diff = [player - opp for player, opp in zip(player["Player_Age"], player["Opponent Age"])] 
    
    win_age = [age for age, result in zip(player["Player_Age"], player["Player Won"]) if result]
    win_age_diff = [diff for diff, result in zip(age_diff, player["Player Won"]) if result]
    loss_age = [age for age, result in zip(player["Player_Age"], player["Player Won"]) if not result]
    loss_age_diff = [diff for diff, result in zip(age_diff, player["Player Won"]) if not result]

    ax.scatter(win_age, win_age_diff, label="Match won", c="deepskyblue", alpha=0.5, s=20)
    ax.scatter(loss_age, loss_age_diff, label="Match lost", c="purple", alpha=0.5, s=20)

ax.set_xticks(np.arange(14, 41, 2))
ax.xaxis.tick_top()
ax.set_xticklabels(np.arange(14, 41, 2), color="gray")
ax.set_xlabel("Williams's\nAge:", color="gray", loc="left")
ax.xaxis.set_label_position("top")

ax.set_yticks([-20, -10, 0, 10, 20])
ax.set_yticklabels(["-20", "-10", "Same age", "+10", "+20 years"], color="gray")
ax.text(-0.01, 17, "Older \n than \n opponent", transform=ax.get_yaxis_transform(), ha="right", va="center", color="gray")
ax.text(-0.01, -17, "Younger \n than \n opponent", transform=ax.get_yaxis_transform(), ha="right", va="center", color="gray")

ax.set_xlim(13.4, 41)
ax.set_ylim(-20.1, 23)
ax.tick_params(axis="both", which="both", color="lightgray")

ax.axhline(y=0, color="black", linewidth=0.8)
ax.legend(loc="upper left", ncol=2, bbox_to_anchor=(0, 1.15), frameon=False)

ax.grid(True, color="lightgray", linewidth=0.8)
ax.spines[:].set_visible(False) 
ax.set_axisbelow(True)

plt.title("Serena Williams's Professional Matches, Age 14 to 40\n\n", fontweight="bold")
plt.tight_layout()

fig.savefig(os.path.join(PATH_TO_OUTPUTS, "serena.png"), bbox_inches="tight")
plt.close(fig)