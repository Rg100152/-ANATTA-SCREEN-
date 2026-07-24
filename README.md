
### ═══ ◆ ANTI-CAPTURE & OVERLAY PROTECTION ◆ ═══
### *Secure Desktop Environment | Capture Blocked*

</div>

---

## 📋 TABLE OF CONTENTS

- [Overview](#overview)
- [Features](#features)
- [Architecture](#architecture)
- [Protection Mechanisms](#protection-mechanisms)
- [Installation](#installation)
- [Usage](#usage)
- [Forensic Overlay](#forensic-overlay)
- [Configuration](#configuration)
- [Security Model](#security-model)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)

---

## OVERVIEW

**ANATTA-SCREEN** (derived from the Buddhist concept of "non-self") is an enterprise-grade **anti-capture and overlay protection system** designed to prevent unauthorized screenshots and screen recording of sensitive CUI (Controlled Unclassified Information) data.

### Core Objectives

- **Prevent Visual Data Theft**: Block PrintScreen, Snipping Tool, and recording attempts
- **Real-Time Threat Detection**: Monitor system events and user actions
- **Forensic Traceability**: Dynamic watermarking for audit trails
- **Zero-Trust Architecture**: Continuous protection of sensitive applications

### Key Benefits

| Capability | Value |
|------------|-------|
| **Anti-Capture** | Blocks screenshots and screen recording |
| **Event Monitoring** | Real-time detection of capture attempts |
| **Forensic Overlay** | Watermarking for user traceability |
| **Session Tracking** | Unique session IDs for auditing |
| **Zero Dependencies** | Pure Python, no external libraries |

---

## FEATURES

### Core Capabilities

#### 🛡️ Anti-Capture Engine
- Blocks PrintScreen key press events
- Prevents Snipping Tool execution
- Detects screen recording attempts
- Disables clipboard capture

#### 🔍 Event Monitoring System
- Real-time system event detection
- Process monitoring for capture tools
- User action tracking
- Active window monitoring

#### 🏷️ Forensic Overlay
- Dynamic user identification
- Session ID tracking
- IP address logging
- Timestamp verification

#### 📊 Session Management
- Unique session identifier generation
- Activity logging
- Audit trail maintenance
- Session isolation

### Technical Specifications

- **Language**: Python 3.8+
- **Dependencies**: None (Pure Standard Library)
- **Platform**: Cross-platform (Linux, macOS, Windows)
- **Interface**: Terminal-based with ANSI colors

---

## ARCHITECTURE

### System Architecture
