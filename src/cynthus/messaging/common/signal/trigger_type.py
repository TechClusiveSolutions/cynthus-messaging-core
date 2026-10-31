"""Signal Trigger Type class for the Cynthus project"""

from enum import Enum


class SignalTriggerType(str, Enum):
    # An actor performed an action (like tapped a button)
    ACTION_PERFORMED: str = 'action_performed'

    # The system detected an anomaly
    ANOMALY_DETECTED: str = 'anomaly_detected'

    # An actor authenticated
    AUTHENTICATION_SUCCEEDED: str = 'authentication_succeeded'

    # An actor failed to authenticate
    AUTHENTICATION_FAILED: str = 'authentication_failed'
   
    # A threshold was reached
    THRESHOLD_REACHED: str = 'threshold_reached'
    
    # A timer expired
    TIMER_EXPIRED: str = 'timer_expired'
