def study_schedule(permanence_period, target_time):
    result = 0

    try:

        for each in permanence_period:
            if (target_time >= each[0] and target_time <= each[1]):
                result += 1
        return result

    except Exception:
        return None

    raise NotImplementedError
