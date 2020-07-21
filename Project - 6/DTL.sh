[
  {
    "dst": "$raw",
    "src": [
      "mlops/covid"
    ],
    "action": "data",
    "settings": {
      "classes_mapping": "default"
    }
  },
  {
    "action": "flip",
    "src": [
      "$raw"
    ],
    "dst": "$raw_fliph",
    "settings": {
      "axis": "vertical"
    }
  },
  {
    "dst": "$data",
    "src": [
      "$raw",
      "$raw_fliph"
    ],
    "action": "multiply",
    "settings": {
      "multiply": 5
    }
  },
  {
    "action": "crop",
    "src": [
      "$data"
    ],
    "dst": "$randocrop",
    "settings": {
      "random_part": {
        "height": {
          "min_percent": 10,
          "max_percent": 40
        },
        "width": {
          "min_percent": 30,
          "max_percent": 80
        },
        "keep_aspect_ratio": false
      }
    }
  },
  {
    "action": "crop",
    "src": [
      "$data"
    ],
    "dst": "$randocrop2",
    "settings": {
      "random_part": {
        "height": {
          "min_percent": 40,
          "max_percent": 90
        },
        "width": {
          "min_percent": 60,
          "max_percent": 90
        },
        "keep_aspect_ratio": false
      }
    }
  },
  {
    "action": "dummy",
    "src": [
      "$raw",
      "$raw_fliph",
      "$randocrop",
      "$randocrop2"
    ],
    "dst": "$out",
    "settings": {}
  },
  {
    "dst": "$precontrast",
    "src": [
      "$out"
    ],
    "action": "multiply",
    "settings": {
      "multiply": 5
    }
  },
  {
    "dst": "$outcontrast",
    "src": [
      "$precontrast"
    ],
    "action": "contrast_brightness",
    "settings": {
      "contrast": {
        "min": 0.5,
        "max": 2,
        "center_grey": false
      },
      "brightness": {
        "min": -50,
        "max": 50
      }
    }
  },
  {
    "dst": [
      "$totrain",
      "$toval"
    ],
    "src": [
      "$outcontrast",
      "$out"
    ],
    "action": "if",
    "settings": {
      "condition": {
        "probability": 0.95
      }
    }
  },
  {
    "dst": "$train",
    "src": [
      "$totrain"
    ],
    "action": "tag",
    "settings": {
      "tag": "train",
      "action": "add"
    }
  },
  {
    "dst": "$val",
    "src": [
      "$toval"
    ],
    "action": "tag",
    "settings": {
      "tag": "val",
      "action": "add"
    }
  },
  {
    "dst": "dogs_augmented-train-val",
    "src": [
      "$train",
      "$val"
    ],
    "action": "supervisely",
    "settings": {}
   }
]