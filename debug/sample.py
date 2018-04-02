def sample(function):
    samples = []
    def wrapper(*args, **quarks):
        sample = dict(enumerate(args), **quarks)
        value = function(*args, **quarks)
        sample['$'] = value
        samples.append(sample)
        return value
    wrapper.samples = samples
    return wrapper
