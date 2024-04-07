# Hola

## Historial de versiones cancino

### v1

Epochs: 8

| Type  | Units | Activation | Dropout |
| ----- | ----- | ---------- | ------- |
| Dense | 400   | relu       | 0.3     |
| Dense | 250   | relu       | 0.2     |
| Dense | 200   | relu       | 0.2     |
| Dense | 100   | relu       | 0.1     |
| Dense | 100   | relu       | N/A     |

### v2

Epochs: 8

| Type  | Units | Activation | Dropout |
| ----- | ----- | ---------- | ------- |
| Dense | 800   | relu       | 0.2     |
| Dense | 800   | relu       | 0.2     |
| Dense | 250   | relu       | 0.15    |

Accuracy: [0.5104601979255676, 0.8399999737739563]

### v3

Epochs: 5

| Type  | Units | Activation | Dropout |
| ----- | ----- | ---------- | ------- |
| Dense | 1000  | relu       | N/A     |
| Dense | 256   | relu       | 0.3     |
| Dense | 128   | relu       | 0.1     |

Accuracy: [0.4940672814846039, 0.8395744562149048]


### v4

Epochs: 15

| Type  | Units | Activation | Dropout |
| ----- | ----- | ---------- | ------- |
| Dense | 190   | relu       | 0.2     |
| Dense | 190   | relu       | 0.2     |

last epoch 
loss: 0.4565 - accuracy: 0.8400 - val_loss: 0.4426 - val_accuracy: 0.8502

Accuracy: [0.4425795376300812, 0.8501595854759216]


### v5

Epochs: 15

| Type  | Units | Activation | Dropout |
| ----- | ----- | ---------- | ------- |
| Dense | 180   | relu       | 0.15    |
| Dense | 180   | relu       | 0.15    |

last epoch
loss: 0.4166 - accuracy: 0.8502 - val_loss: 0.4541 - val_accuracy: 0.8502

Accuracy: [0.44653087854385376, 0.8504787087440491]